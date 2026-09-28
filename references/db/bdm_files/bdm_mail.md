# 邮箱设置-bdm_mail

## 企业信息-子表 t_bdm_mail_items

- **表名称：** 企业信息-子表
- **表名：** t_bdm_mail_items

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | fepinfo | 企业信息 | int8 | 64 |  | √ | 0 | [企业基础信息 bdm_enterprise_baseinfo](../bdm_files/bdm_enterprise_baseinfo.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bdm_mail_items |  | fid |
| 2 | pk_t_bdm_mail_items |  | fentryid |

---

## 邮箱设置-主表 t_bdm_mail_setting

- **表名称：** 邮箱设置-主表
- **表名：** t_bdm_mail_setting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 方案名称 | varchar | 50 |  | √ | ' ' | 方案名称 |
| 3 | fmailtempoption | 邮箱模板选项 | varchar | 50 |  | √ | ' ' | 邮箱模板选项,枚举: 1 :自定义样式 0 :默认样式 |
| 4 | fmailbody_tag | 富文本编辑器_详情 | text | 0 |  |  | null | 富文本编辑器_详情 |
| 5 | fpassword | 密码 | varchar | 50 |  | √ | ' ' | 密码 |
| 6 | fstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: 0 :禁用 1 :启用 |
| 7 | fusername | 用户账号 | varchar | 50 |  | √ | ' ' | 用户账号 |
| 8 | fmailbody | 富文本编辑器 | varchar | 255 |  | √ | ' ' | 富文本编辑器 |
| 9 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 10 | fepinfos | 分配企业 | varchar | 2000 |  | √ | ' ' | 分配企业 |
| 11 | fsendinvoiceoption | 电子发票推送按钮组 | varchar | 50 |  | √ | ' ' | 电子发票推送按钮组,枚举: 0 :系统邮箱 1 :自定义邮箱 |
| 12 | fseparator | 分隔符选择 | varchar | 50 |  | √ | ' ' | 分隔符选择,枚举: 0 :_ 1 :& 2 :- 3 :. 4 :* |
| 13 | fserveraddress | 服务器地址 | varchar | 50 |  | √ | ' ' | 服务器地址 |
| 14 | fssl | SSL加密 | bpchar | 1 |  | √ | ' ' | SSL加密 |
| 15 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fport | 端口号 | int8 | 64 |  | √ | 0 | 端口号 |
| 17 | fnumber | 编号 | varchar | 50 |  | √ | ' ' | 编号 |
| 18 | fclientname | 用户名 | varchar | 50 |  | √ | ' ' | 用户名 |
| 19 | fmailtitle | 邮箱主题 | varchar | 50 |  | √ | ' ' | 邮箱主题 |
| 20 | fpushmailtype | fpushmailtype | varchar | 50 |  | √ | ' ' |  |
| 21 | fnowfilename | 命名规则 | varchar | 50 |  | √ | ' ' | 命名规则 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdm_mail_setting |  | fid |
| 2 | idx_bdm_mail_setting |  | fnumber |
