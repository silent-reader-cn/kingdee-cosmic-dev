# 规则设计（规则引擎）-plm_rengine_ruledesign

## 行政组织-多选基础资料表 t_plm_egn_ruleadminorg

- **表名称：** 行政组织-多选基础资料表
- **表名：** t_plm_egn_ruleadminorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | varchar | 50 |  | √ | ' ' | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_egn_ruleadminorg |  | fid,fbasedataid |
| 2 | pk_plm_egn_ruleadminorg |  | fpkid |

---

## 规则设计（规则引擎）-多语言表 t_plm_egn_drlfilter_l

- **表名称：** 规则设计（规则引擎）-多语言表
- **表名：** t_plm_egn_drlfilter_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fname | 规则名称 | varchar | 100 |  | √ | ' ' | 规则名称 |
| 2 | fsimplename | 简称 | varchar | 100 |  | √ | ' ' | 简称 |
| 3 | fruledescription | fruledescription | varchar | 255 |  | √ | ' ' |  |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fdescription | 规则描述 | varchar | 255 |  | √ | ' ' | 规则描述 |
| 6 | frulename | 规则名称 | varchar | 255 |  | √ | ' ' | 规则名称 |
| 7 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_drlfilter_l |  | fentryid,flocaleid |
| 2 | pk_plm_egn_drlfilter_l |  | fpkid |

---

## 规则设计（规则引擎）-主表 t_plm_egn_drlfilter

- **表名称：** 规则设计（规则引擎）-主表
- **表名：** t_plm_egn_drlfilter

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 所属策略 | int8 | 64 |  | √ | 0 | [策略管理 plm_rengine_policy](../plmsm_files/plm_rengine_policy.md) |
| 2 | ftemplatenumber | 模板编码 | varchar | 100 |  | √ | ' ' | 模板编码 |
| 3 | fseq | 排序号 | int8 | 64 |  | √ | 0 | 排序号 |
| 4 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 5 | frulescene | frulescene | int8 | 64 |  | √ | 0 |  |
| 6 | ffilterresult | ffilterresult | text | 0 |  |  | ' ' |  |
| 7 | fbizappid | 所属应用 | varchar | 18 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 2 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fsceneid | 所属场景 | int8 | 64 |  | √ | 0 | [场景管理 plm_rengine_scene](../plmsm_files/plm_rengine_scene.md) |
| 13 | fruledescription | fruledescription | varchar | 255 |  | √ | ' ' |  |
| 14 | fissyspreset | 是否系统预置 | bpchar | 1 |  | √ | '0' | 是否系统预置 |
| 15 | fruleorder | 优先级 | int8 | 64 |  | √ | 0 | 优先级 |
| 16 | fname | 规则名称 | varchar | 100 |  | √ | ' ' | 规则名称 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fruleenable | fruleenable | bpchar | 1 |  | √ | '1' |  |
| 20 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fdescription | 规则描述 | varchar | 255 |  | √ | ' ' | 规则描述 |
| 22 | frulenumber | 规则编码 | varchar | 50 |  | √ | ' ' | 规则编码 |
| 23 | fresultpreview | fresultpreview | varchar | 50 |  | √ | ' ' |  |
| 24 | fresults | 结果 | text | 0 |  |  | null | 结果 |
| 25 | fsimplename | 简称 | varchar | 100 |  | √ | ' ' | 简称 |
| 26 | fenable | 使用状态 | varchar | 2 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 10 :待启用 |
| 27 | fconditionpreview | fconditionpreview | varchar | 50 |  | √ | ' ' |  |
| 28 | frulebizapp | frulebizapp | varchar | 36 |  | √ | ' ' |  |
| 29 | fnumber | 规则编码 | varchar | 50 |  | √ | ' ' | 规则编码 |
| 30 | frulename | 规则名称 | varchar | 255 |  | √ | ' ' | 规则名称 |
| 31 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 32 | fconditions | 条件 | text | 0 |  |  | null | 条件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_drlfilter |  | fid |
| 2 | pk_plm_egn_drlfilter |  | fentryid |
