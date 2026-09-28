# 一键报销设置-er_invoicepginfo

## 一键报销设置-多语言表 t_er_invoicepginfo_l

- **表名称：** 一键报销设置-多语言表
- **表名：** t_er_invoicepginfo_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 操作名称 | varchar | 255 |  | √ | ' ' | 操作名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_invoicepginfo_l |  | fpkid |
| 2 | idx_er_invoicepginfo_l_fid |  | fid,flocaleid |

---

## 一键报销设置-主表 t_er_invoicepginfo

- **表名称：** 一键报销设置-主表
- **表名：** t_er_invoicepginfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fpluginpath | 插件路径 | varchar | 255 |  | √ | ' ' | 插件路径 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fclienttype | 客户端类型 | varchar | 50 |  | √ | ' ' | 客户端类型,枚举: 0 :移动端 1 :PC端 |
| 6 | fbillgroup | 单据类型 | int8 | 64 |  | √ | 0 | 单据设置 er_setting_group |
| 7 | fbillname | fbillname | varchar | 50 |  | √ | ' ' |  |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fclicksign | 控件标识 | varchar | 255 |  | √ | ' ' | 控件标识 |
| 10 | fbizitem | 业务事项 | int8 | 64 |  | √ | 0 | 业务事项 er_standard_type |
| 11 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fenable | 是否启用 | varchar | 50 |  | √ | '0' | 是否启用,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 编码 | varchar | 255 |  | √ | ' ' | 编码 |
| 16 | fbilltype | 单据类型(废弃) | varchar | 50 |  | √ | ' ' | 单据类型(废弃),枚举: er_tripreimbursebill :差旅报销单(卡片式) er_tripreimbill_grid :差旅报销单(表格式) er_dailyreimbursebill :费用报销单 er_publicreimbursebill :对公报销单 er_dailyreimbursebill_B :移动话费报销单 er_dailyreimbursebill_A :额度报销单 er_checkingpaybill :商旅付款申请单 er_expense_recordbill :记费用 er_trip_recordbill :记差旅 er_publicreimbursebill_asset :资产报账单 |
| 17 | fisdefault | 默认 | bpchar | 1 |  | √ | '0' | 默认 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_invpginfo_fnumber |  | fnumber |
| 2 | idx_invpginfo_billclient |  | fclienttype,fbilltype |
| 3 | pk_t_er_invoicepginfo |  | fid |
