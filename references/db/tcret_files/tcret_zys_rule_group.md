# 资源税规则配置分组列表-tcret_zys_rule_group

## 资源税规则配置分组列表-主表 t_tcret_all_rule_config

- **表名称：** 资源税规则配置分组列表-主表
- **表名：** t_tcret_all_rule_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 适用取数规则 | int8 | 64 |  | √ | 0 | [规则类型树形基础资料 tdm_rule_type_tree](../tdm_files/tdm_rule_type_tree.md) |
| 3 | fyhssubitem | 印花税子目 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tcsd_bizdef_entry |
| 4 | ftaxitem | 税目 | int8 | 64 |  | √ | 0 | 资源税税率表分录 tpo_zys_taxitem_entry |
| 5 | fruletype | 规则类型 | varchar | 50 |  | √ | ' ' | 规则类型,枚举: private :自用规则 public :可分配规则 |
| 6 | ftaxation | 征收方式 | varchar | 50 |  | √ | ' ' | 征收方式,枚举: aqhz :按期汇总 hdzs :核定征收 |
| 7 | fsubitem | 子目 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tcsd_bizdef_entry |
| 8 | forg | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fyhstaxitem | 印花税税目 | int8 | 64 |  | √ | 0 | 印花税税率（树） tpo_tcsd_taxrateentrytree |
| 11 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fzystaxitem | 资源税税目 | int8 | 64 |  | √ | 0 | 资源税税率表分录 tpo_zys_taxitem_entry |
| 15 | fleasecontractno | 租赁项目编号 | int8 | 64 |  | √ | 0 | [房产出租信息 tdm_house_rental_info](../tdm_files/tdm_house_rental_info.md) |
| 16 | ftaxitemtype | 税目类型 | varchar | 50 |  | √ | ' ' | 税目类型,枚举: tpo_zys_taxitem_entry :资源税税率表分录 |
| 17 | fname | 规则名称 | varchar | 200 |  | √ | ' ' | 规则名称 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fsubitemtype | 子目类型 | varchar | 50 |  | √ | ' ' | 子目类型,枚举: tpo_tcsd_bizdef_entry :业务定义分录 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | ftaxsubitem | 子目 | varchar | 50 |  | √ | ' ' | 子目,枚举: yk :原矿 xk :选矿 |
| 22 | fxtys | 系统预设 | varchar | 50 |  | √ | ' ' | 系统预设,枚举: 1 :是 0 :否 |
| 23 | fdeclaretype | 申报期限类型 | varchar | 50 |  | √ | ' ' | 申报期限类型,枚举: aqsb :按期申报 acsb :按次申报 |
| 24 | ftaxsource | 税源编号 | int8 | 64 |  | √ | 0 | [资源税税源登记信息 tcret_zys_register](../tcret_files/tcret_zys_register.md) |
| 25 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 26 | fnumber | 规则编码 | varchar | 30 |  | √ | ' ' | 规则编码 |
| 27 | frulepurpose | 规则用途 | varchar | 50 |  | √ | ' ' | 规则用途,枚举: nssb :纳税申报 sjjt :税金计提 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcret_all_rule_config |  | fid |
| 2 | idx_tcret_all_rule_config |  | fnumber |

---

## 资源税规则配置分组列表-多语言表 t_tcret_all_rule_config_l

- **表名称：** 资源税规则配置分组列表-多语言表
- **表名：** t_tcret_all_rule_config_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 规则名称 | varchar | 200 |  | √ | ' ' | 规则名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcret_all_rule_config_l_0 |  | fid,flocaleid |
| 2 | pk_tcret_all_rule_config_l |  | fpkid |
