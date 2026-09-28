# 短信推送权限控制设置-bdm_msg_auth_setting

## 短信推送权限控制设置-主表 t_bdm_msg_auth_setting

- **表名称：** 短信推送权限控制设置-主表
- **表名：** t_bdm_msg_auth_setting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcheckemail | 邮箱校验 | bpchar | 1 |  | √ | ' ' | 邮箱校验 |
| 3 | fpushmessagecenter | fpushmessagecenter | bpchar | 1 |  | √ | ' ' |  |
| 4 | fmsgswitch | 短信推送服务 | bpchar | 1 |  | √ | ' ' | 短信推送服务 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fcheckphone | 下拉列表 | bpchar | 1 |  | √ | ' ' | 下拉列表,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bdm_msg_auth_setting |  | fmsgswitch |
| 2 | pk_bdm_msg_auth_setting |  | fid |
