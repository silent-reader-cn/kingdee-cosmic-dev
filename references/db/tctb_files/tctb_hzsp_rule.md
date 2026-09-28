# 汇总审批规则-tctb_hzsp_rule

## 单据体-子表 t_tctb_hzsp_rule_config

- **表名称：** 单据体-子表
- **表名：** t_tctb_hzsp_rule_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forgdesc | 组织字段 | bpchar | 1 |  | √ | '0' | 组织字段 |
| 3 | fhzspbilllist | fhzspbilllist | bpchar | 1 |  | √ | '0' |  |
| 4 | ffieldname | 字段名称 | varchar | 50 |  | √ | ' ' | 字段名称 |
| 5 | fbizsubname | 业务名称 | varchar | 50 |  | √ | ' ' | 业务名称 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fhzspbillgroup | 汇总审批单分组字段 | varchar | 50 |  | √ | ' ' | 汇总审批单分组字段 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctb_hzsp_rule_config_fk |  | fid |
| 2 | pk_tctb_hzsp_rule_config |  | fentryid |

---

## 汇总审批规则-主表 t_tctb_hzsp_rule

- **表名称：** 汇总审批规则-主表
- **表名：** t_tctb_hzsp_rule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdescribe | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 3 | fuseorg | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 5 | fsrccreateorgid | fsrccreateorgid | int8 | 64 |  | √ | 0 |  |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fhzspruletype | 汇总审批规则类型 | int8 | 64 |  | √ | 0 | [汇总审批规则类型 tctb_hzsp_rule_type](../tctb_files/tctb_hzsp_rule_type.md) |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fitemclasstypefield | fitemclasstypefield | varchar | 50 |  | √ | ' ' |  |
| 12 | fsourcedataid | fsourcedataid | int8 | 64 |  | √ | 0 |  |
| 13 | fissystem | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 14 | fbitindex | fbitindex | int8 | 64 |  | √ | 0 |  |
| 15 | fsubmitted | 直接提交 | bpchar | 1 |  | √ | '0' | 直接提交 |
| 16 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fctrlstrategy | fctrlstrategy | varchar | 50 |  | √ | ' ' |  |
| 21 | fitemclassfield | fitemclassfield | int8 | 64 |  | √ | 0 |  |
| 22 | fhzspbilltype | 汇总审批单据类型 | int8 | 64 |  | √ | 0 | [汇总审批单据类型 tctb_hzsp_bill_type](../tctb_files/tctb_hzsp_bill_type.md) |
| 23 | ftaskstartmethod | 任务发起方式 | varchar | 50 |  | √ | ' ' | 任务发起方式,枚举: lbymgxdj :列表页面勾选单据 lbymbgxdj :列表页面不勾选单据 |
| 24 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 25 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 26 | fsourcebitindex | fsourcebitindex | int8 | 64 |  | √ | 0 |  |
| 27 | fapprovalmethod | 审批方式 | varchar | 50 |  | √ | ' ' | 审批方式,枚举: plsp :批量审批 hzsp :汇总审批 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctb_hzsp_rule |  | fid |
| 2 | idx_t_tctb_hzsp_rule_master |  | fmasterid |
| 3 | idx_t_tctb_hzsp_rule_createorg |  | fcreateorgid |

---

## 汇总审批规则-多语言表 t_tctb_hzsp_rule_l

- **表名称：** 汇总审批规则-多语言表
- **表名：** t_tctb_hzsp_rule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 50 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 50 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctb_hzsp_rule_l |  | fpkid |
| 2 | idx_tctb_hzsp_rule_l_0 |  | fid,flocaleid |
