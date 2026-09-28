# 经销商门户登录信息-ocepfp_logininfo

## 经销商门户登录信息-主表 t_ocepfp_logininfo

- **表名称：** 经销商门户登录信息-主表
- **表名：** t_ocepfp_logininfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fiscustomtheme | 是否自定义主题 | bpchar | 1 |  | √ | '0' | 是否自定义主题 |
| 3 | fthemecolor | 主题色 | varchar | 50 |  | √ | ' ' | 主题色 |
| 4 | fpageopentype | 页面打开方式 | varchar | 50 |  | √ | ' ' | 页面打开方式 |
| 5 | flogintime | 登录日期 | timestamp | 0 |  |  | null | 登录日期 |
| 6 | fisdefaluttheme | 是否默认主题 | bpchar | 1 |  | √ | '0' | 是否默认主题 |
| 7 | fuserid | 用户 | int8 | 64 |  | √ | 0 | 用户信息 bos_usergroup_user |
| 8 | ftabshowtype | 内容排版方式 | varchar | 50 |  | √ | ' ' | 内容排版方式 |
| 9 | fsupplierid | 供货方 | int8 | 64 |  | √ | 0 | 供货关系 ocdbd_channel_authorize |
| 10 | fcustomerid | 当前登录渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocepfp_logininfo_user |  | fuserid |
| 2 | pk_ocepfp_logininfo |  | fid |
