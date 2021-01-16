import React from 'react';
import Container from '@material-ui/core/Container';
import { makeStyles } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';
import Link from '@material-ui/core/Link';
import Box from '@material-ui/core/Box';

const useStyles = makeStyles((theme) => ({
	'@global': {
		ul: {
			margin: 0,
			padding: 0,
			listStyle: 'none',
		},
	},
	footer: {
		borderTop: `2px solid ${theme.palette.divider}`,
		marginTop: theme.spacing(8),
		paddingTop: theme.spacing(3),
		paddingBottom: theme.spacing(3),
	},
}));

function Copyright() {
	return (
		<Typography variant="body2" color="textSecondary" align="center">
			{'Copyright © Ariel Sashcov '}
            {new Date().getFullYear()}
            {' • '}
			<Link color="inherit" href="https://docs.google.com/document/d/1ZKRywXQLZWOqVOHC4JkF3LqdpO3Llpfk_CkZPR8bjak/edit#heading=h.n7bww7g70ipk">
				Shopify Summer 2021 Developer Intern Challenge
			</Link>
            {' '}
			{'.'}
		</Typography>
	);
}

function Footer() {
	const classes = useStyles();
	return (
		<React.Fragment>
			<Container maxWidth="md" component="footer" className={classes.footer}>
				<Box mt={2}>
					<Copyright />
				</Box>
			</Container>
		</React.Fragment>
	);
}

export default Footer;
