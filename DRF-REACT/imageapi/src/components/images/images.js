import React from "react"
import { makeStyles } from "@material-ui/core/styles"
import Card from "@material-ui/core/Card"
import CardContent from "@material-ui/core/CardContent"
import CardMedia from "@material-ui/core/CardMedia"
import Grid from "@material-ui/core/Grid"
import Typography from "@material-ui/core/Typography"
import Container from "@material-ui/core/Container"
import Link from "@material-ui/core/Link"

const useStyles = makeStyles((theme) => ({
    cardMedia: {
        paddingTop: "56.25%", // 16:9
    },
    link: {
        margin: theme.spacing(1, 1.5),
    },
    cardHeader: {
        backgroundColor:
            theme.palette.type === "light"
                ? theme.palette.grey[200]
                : theme.palette.grey[700],
    },
    imageTitle: {
        fontSize: "16px",
        textAlign: "left",
    },
    imageText: {
        display: "flex",
        justifyContent: "left",
        alignItems: "baseline",
        fontSize: "12px",
        textAlign: "left",
        marginBottom: theme.spacing(2),
    },
}))

const Images = (props) => {
    const { images } = props
    const classes = useStyles()
    if (!images || images.length === 0)
        return <p>Can not find any images, sorry</p>
    return (
        <React.Fragment>
            <Container maxWidth="md" component="main">
                <Grid container spacing={5} alignItems="flex-end">
                    {images.map((image) => {
                        return (
                            // Enterprise card is full width at sm breakpoint
                            <Grid item key={image.id} xs={12} md={4}>
                                <Card className={classes.card}>
                                    <Link
                                        color="textPrimary"
                                        href={"images/" + image.slug}
                                        className={classes.link}
                                    >
                                        <CardMedia
                                            className={classes.cardMedia}
                                            image={image.image}
                                            title={image.title}
                                        />
                                    </Link>
                                    <CardContent
                                        className={classes.cardContent}
                                    >
                                        <Typography
                                            gutterBottom
                                            variant="h6"
                                            component="h2"
                                            className={classes.imageTitle}
                                        >
                                            {image.title}
                                        </Typography>
                                    </CardContent>
                                </Card>
                            </Grid>
                        )
                    })}
                </Grid>
            </Container>
        </React.Fragment>
    )
}
export default Images
