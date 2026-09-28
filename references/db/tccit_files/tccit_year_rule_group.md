# 年报申报项规则配置-tccit_year_rule_group

## 年报申报项规则配置-主表 t_tccit_all_rule_config

- **表名称：** 年报申报项规则配置-主表
- **表名：** t_tccit_all_rule_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 规则名称 | varchar | 200 |  | √ | ' ' | 规则名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fgroupid | 适用取数规则 | int8 | 64 |  | √ | 0 | [规则类型树形基础资料 tdm_rule_type_tree](../tdm_files/tdm_rule_type_tree.md) |
| 5 | fspap | 自产/外购 | varchar | 50 |  | √ | ' ' | 自产/外购,枚举: self :自产 out :外购 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fruletype | 规则类型 | varchar | 50 |  | √ | ' ' | 规则类型,枚举: private :自用规则 public :可分配规则 |
| 8 | forg | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fitemid | 取数项目选择 | int8 | 64 |  | √ | 0 | 优惠项目（树） tpo_discount_tree |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fitemtype | 取数项目类型 | varchar | 50 |  | √ | ' ' | 取数项目类型,枚举: tpo_discount_tree :优惠项目（树） tpo_yearitems_tree :项目取数（树） tpo_standingbook_tree :台账项目（树） |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fissystem | 系统预设 | varchar | 50 |  | √ | '0' | 系统预设,枚举: 0 :否 1 :是 |
| 16 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :已禁用 1 :已启用 |
| 17 | fnumber | 规则编码 | varchar | 30 |  | √ | ' ' | 规则编码 |
| 18 | frulepurpose | 规则用途 | varchar | 50 |  | √ | ' ' | 规则用途,枚举: nssb :纳税申报 sjjt :税金计提 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_all_rule_cfg_fnumber |  | fnumber |
| 2 | pk_tccit_all_rule_config |  | fid |

---

## 年报申报项规则配置-多语言表 t_tccit_all_rule_config_l

- **表名称：** 年报申报项规则配置-多语言表
- **表名：** t_tccit_all_rule_config_l

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
| 1 | pk_tccit_all_rule_config_l |  | fpkid |
| 2 | idx_tccit_all_rule_config_l_0 |  | fid,flocaleid |
