import React from 'react'
import PropTypes from 'prop-types'

const Button = ({
  children,
  disabled = false,
  loading = false,
  variant = 'primary',
  icon,
  onClick,
  ...props
}) => {
  return (
    <button
      className={`button ${variant} ${disabled ? 'disabled' : ''} ${loading ? 'loading' : ''} ${icon ? 'has-icon' : ''}`}
      disabled={disabled || loading}
      onClick={onClick}
      {...props}
    >
      {icon && <span className="icon">{icon}</span>}
      {loading ? (
        <>
          <span className="spinner">⌛</span>
          {children}
        </>
      ) : (
        children
      )}
    </button>
  )
}

Button.propTypes = {
  children: PropTypes.node.isRequired,
  disabled: PropTypes.bool,
  loading: PropTypes.bool,
  variant: PropTypes.oneOf(['primary', 'secondary', 'danger']),
  icon: PropTypes.string,
  onClick: PropTypes.func,
}

export default Button 