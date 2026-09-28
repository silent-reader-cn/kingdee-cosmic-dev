# 经营数据授权-xkoac_dataauth

## 经营单元子单据体-子表 t_xkoac_authuserunit

- **表名称：** 经营单元子单据体-子表
- **表名：** t_xkoac_authuserunit

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 4 | fauthunitid | 经营单元 | int8 | 64 |  | √ | 0 | [经营单元 xkoac_unit](../basedata_files/xkoac_unit.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkoac_authentry |  | fentryid |
| 2 | pk_xkoac_authuserunit |  | fdetailid |

---

## 经营数据授权-主表 t_xkoac_auth

- **表名称：** 经营数据授权-主表
- **表名：** t_xkoac_auth

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 经营组织架构 | int8 | 64 |  | √ | 0 | [经营组织架构 xkoac_orgsystemgroup](../xkoac_files/xkoac_orgsystemgroup.md) |
| 6 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fbookid | 经营账簿 | int8 | 64 |  | √ | 0 | [经营账簿 xkoac_operatingbook](../xkoac_files/xkoac_operatingbook.md) |
| 8 | faudittime | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fdisabletime | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fauthrange | 授权范围 | bpchar | 1 |  | √ | ' ' | 授权范围,枚举: 1 :经营单元 |
| 15 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fauthtype | 授权类型 | bpchar | 1 |  | √ | '1' | 授权类型,枚举: 1 :用户 2 :角色 |
| 17 | fnumber | 编码 | varchar | 255 |  | √ | ' ' | 编码 |
| 18 | fbizobj | 业务对象 | varchar | 2000 |  | √ | ' ' | 业务对象,枚举: xkoaca_rpt :自定义报表 xkoac_amoebabalance :资产负债余额表 xkoac_profitdetail :经营利润表 xkoac_profitsum :经营利润汇总表 xkoac_profithorizon :经营利润横向展示表 xkoac_dimensionprofit :经营核算维度利润表 xkoac_voucher :经营流水账 xkoac_businessplan :经营计划单 xkoac_instatement :经营单元内部结算单 xkoac_settleprice :经营单元结算价目表 xkoac_costcollecte :经营费用归集单 xkoac_allocationresults :经营费用分摊结果单 |
| 19 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkoac_auth |  | fid |
| 2 | idx_xkoac_auth_book |  | fbookid |

---

## 经营数据授权-多语言表 t_xkoac_auth_l

- **表名称：** 经营数据授权-多语言表
- **表名：** t_xkoac_auth_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkoac_auth_l |  | fid,flocaleid |
| 2 | pk_xkoac_auth_l |  | fpkid |

---

## 用户单据体-子表 t_xkoac_authuser

- **表名称：** 用户单据体-子表
- **表名：** t_xkoac_authuser

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fauthuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fauthroleid | 角色 | varchar | 36 |  | √ | ' ' | [通用角色 perm_role](../base_files/perm_role.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkoac_authuser |  | fauthuserid |
| 2 | idx_xkoac_authrole |  | fauthroleid |
| 3 | pk_xkoac_authuser |  | fentryid |
