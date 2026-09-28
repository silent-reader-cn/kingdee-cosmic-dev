# 隐私签署管理-chatbi_privacy_agreement

## 隐私签署管理-主表 t_cbi_privacy_management

- **表名称：** 隐私签署管理-主表
- **表名：** t_cbi_privacy_management

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | flegaldocument | 法律文件 | varchar | 50 |  | √ | ' ' | 法律文件 |
| 3 | fusername | fusername | varchar | 50 |  | √ | ' ' |  |
| 4 | fname | fname | varchar | 50 |  | √ | ' ' |  |
| 5 | fcreaterfield | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fprivacystatus | 签署状态 | varchar | 50 |  | √ | '0' | 签署状态,枚举: 0 :未同意 1 :同意 |
| 7 | fopertime | 操作时间 | timestamp | 0 |  |  | LOCALTIMESTAMP | 操作时间 |
| 8 | furl | 隐私协议URL | varchar | 250 |  | √ | ' ' | 隐私协议URL |
| 9 | fishistorical | 是否历史签署记录 | varchar | 50 |  | √ | 'A' | 是否历史签署记录,枚举: |
| 10 | fversion | 隐私版本 | varchar | 50 |  | √ | ' ' | 隐私版本 |
| 11 | fbusinessobj | 业务对象 | varchar | 50 |  | √ | ' ' | 业务对象 |
| 12 | fcode | 隐私协议代码 | varchar | 50 |  | √ | ' ' | 隐私协议代码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cbi_privacy_management |  | fid |
