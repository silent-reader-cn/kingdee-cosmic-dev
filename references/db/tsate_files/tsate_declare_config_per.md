# 个税税局登录配置-tsate_declare_config_per

## 个税税局登录配置-主表 t_tsate_declare_config_pe

- **表名称：** 个税税局登录配置-主表
- **表名：** t_tsate_declare_config_pe

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | frealnamepassword | 实名密码 | varchar | 50 |  | √ | ' ' | 实名密码 |
| 6 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fdeclarepassword | 申报密码 | varchar | 50 |  | √ | ' ' | 申报密码 |
| 8 | flogintype | 税局登录验证方式 | varchar | 50 |  | √ | ' ' | 税局登录验证方式,枚举: 2 :用户名密码登录 9 :申报密码登录 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | frealnameaccount | 实名账号 | varchar | 50 |  | √ | ' ' | 实名账号 |
| 12 | ftaxorganid | 主管税务机关 | int8 | 64 |  | √ | 0 | [税务机关 bastax_taxorgan](../bastax_files/bastax_taxorgan.md) |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | ftaxofficelocation | 申报税局所在地 | int8 | 64 |  | √ | 0 | [税企直连行政区化配置 tsate_areainfo_setting](../tsate_files/tsate_areainfo_setting.md) |
| 15 | flogincategory | 登陆类型 | int8 | 64 |  | √ | 0 | [登陆类型 tsate_login_type](../tsate_files/tsate_login_type.md) |
| 16 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fbillno | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 18 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tsate_declare_config_pe |  | forgid |
| 2 | pk_tsate_declare_config_pe |  | fid |
