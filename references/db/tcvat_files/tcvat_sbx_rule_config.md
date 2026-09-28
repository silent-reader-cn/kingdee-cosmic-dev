# 申报项规则配置-tcvat_sbx_rule_config

## 申报项规则配置-多语言表 t_tcvat_all_rule_config_l

- **表名称：** 申报项规则配置-多语言表
- **表名：** t_tcvat_all_rule_config_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 规则名称 | varchar | 400 |  | √ | ' ' | 规则名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_all_rule_config_l |  | fid,flocaleid |
| 2 | pk_tcvat_all_rule_config_l |  | fpkid |

---

## 申报项规则配置-主表 t_tcvat_all_rule_config

- **表名称：** 申报项规则配置-主表
- **表名：** t_tcvat_all_rule_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 适用取数规则 | int8 | 64 |  | √ | 0 | [规则类型树形基础资料 tdm_rule_type_tree](../tdm_files/tdm_rule_type_tree.md) |
| 3 | fmdtype | 退税类型 | varchar | 50 |  | √ | ' ' | 退税类型,枚举: mdt :免抵退应退税额 md :增值税免抵税额 jzjtsjtse :即征即退实际退税额 |
| 4 | fhyncp | fhyncp | int8 | 64 |  | √ | 0 |  |
| 5 | fruletype | 规则类型 | varchar | 50 |  | √ | ' ' | 规则类型,枚举: private :自用规则 public :可分配规则 |
| 6 | fdeductproject | 扣除项目 | varchar | 50 |  | √ | ' ' | 扣除项目,枚举: bqfse :本期发生额 bqsjkce :本期实际扣除额 fseandkce :本期发生额和实际扣除额 |
| 7 | fjzjtlx | 即征即退类型 | varchar | 50 |  | √ | ' ' | 即征即退类型,枚举: jzjt :即征即退 wfhf :无法划分 |
| 8 | forg | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fjzjt | 即征即退业务 | varchar | 50 |  | √ | ' ' | 即征即退业务,枚举: 0 :否 1 :是 2 :无法划分 |
| 11 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fwfhfzclx | fwfhfzclx | varchar | 50 |  | √ | ' ' |  |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | frate | frate | varchar | 50 |  | √ | ' ' |  |
| 16 | fissystem | 系统预设 | varchar | 50 |  | √ | ' ' | 系统预设,枚举: 0 :否 1 :是 |
| 17 | freductiontype | 减税项目类型 | varchar | 50 |  | √ | ' ' | 减税项目类型,枚举: 1 :免税 2 :减征 3 :扣减 4 :抵减 5 :即征即退 6 :其他 |
| 18 | ftaxrateid | 税率/征收率 | int8 | 64 |  | √ | 0 | 税率模板 tpo_tcvat_taxrates |
| 19 | ftaxpayertype | 适用纳税人类型 | varchar | 50 |  | √ | ' ' | 适用纳税人类型,枚举: ybnsr :一般纳税人 xgmnsr :小规模纳税人 |
| 20 | ftaxationid | 征收方式 | int8 | 64 |  | √ | 0 | 征收方式模板 tpo_tcvat_taxperiod |
| 21 | fname | 规则名称 | varchar | 200 |  | √ | ' ' | 规则名称 |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fdhzsfs | fdhzsfs | varchar | 50 |  | √ | ' ' |  |
| 24 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 25 | fdeducttype | 抵扣类型 | int8 | 64 |  | √ | 0 | 业务定义 tpo_tcvat_bizdef |
| 26 | fcpmc | fcpmc | int8 | 64 |  | √ | 0 |  |
| 27 | fylfl | fylfl | varchar | 50 |  | √ | ' ' |  |
| 28 | frefundtype | frefundtype | int8 | 64 |  | √ | 0 |  |
| 29 | frollouttype | 转出类型 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tcvat_bizdef_entity |
| 30 | fdifftype | 差额扣除类型 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tcvat_bizdef_entity |
| 31 | fsign | fsign | varchar | 50 |  | √ | ' ' |  |
| 32 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :已禁用 1 :已启用 |
| 33 | fnumber | 规则编码 | varchar | 30 |  | √ | ' ' | 规则编码 |
| 34 | fprepayproject | 预缴项目名称 | int8 | 64 |  | √ | 0 | [预缴项目信息 tcvat_prepay_project_info](../tcvat_files/tcvat_prepay_project_info.md) |
| 35 | frulename | frulename | int8 | 64 |  | √ | 0 |  |
| 36 | frulepurpose | 规则用途 | varchar | 50 |  | √ | ' ' | 规则用途,枚举: nssb :纳税申报 sjjt :税金计提 |
| 37 | fperpreproduct | 分次预缴项目类型 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tcvat_bizdef_entity |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvatallruleconfig_number |  | fnumber |
| 2 | pk_tcvat_all_rule_config |  | fid |
