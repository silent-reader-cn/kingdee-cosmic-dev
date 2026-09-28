# 报销流程服务插件配置-er_reimservicepg

## 报销流程服务插件配置-主表 t_er_reimservicepg

- **表名称：** 报销流程服务插件配置-主表
- **表名：** t_er_reimservicepg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fclassname | 流程插件 | varchar | 255 |  | √ | ' ' | 流程插件 |
| 6 | fclienttype | 客户端类型 | varchar | 50 |  | √ | ' ' | 客户端类型,枚举: 0 :移动端 1 :PC端 |
| 7 | fbillgroup | 单据类型 | int8 | 64 |  | √ | 0 | [单据设置 er_setting_group](../em_files/er_setting_group.md) |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fbizitem | fbizitem | int8 | 64 |  | √ | 0 |  |
| 10 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 15 | fformid | 表单id | varchar | 255 |  | √ | ' ' | 表单id |
| 16 | fbilltype | 单据类型 | varchar | 50 |  | √ | ' ' | 单据类型,枚举: er_tripreimbursebill :差旅报销单(卡片式) er_tripreimbill_grid :差旅报销单(表格式) er_dailyreimbursebill :费用报销单 er_publicreimbursebill :对公报销单 er_dailyreimbursebill_B :移动话费报销单 er_dailyreimbursebill_A :额度报销单 er_checkingpaybill :商旅付款申请单 er_expense_recordbill :记费用 er_trip_recordbill :记差旅 er_publicreimbursebill_asset :资产报账单 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_reimservice_number |  | fnumber |
| 2 | idx_er_reimservice_clustered |  | fclienttype,fname |
| 3 | idx_er_resercfg_cli |  | fclienttype,fname |
| 4 | pk_t_er_reimservicepg |  | fid |

---

## 报销流程服务插件配置-多语言表 t_er_reimservicepg_l

- **表名称：** 报销流程服务插件配置-多语言表
- **表名：** t_er_reimservicepg_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_reimservicepg_l |  | fpkid |
