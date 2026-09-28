# 规则列表（规则引擎）-plm_rengine_rulelist

## 规则信息分录-多语言表 t_plm_egn_drlfilter_l

- **表名称：** 规则信息分录-多语言表
- **表名：** t_plm_egn_drlfilter_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 2 | fsimplename | fsimplename | varchar | 100 |  | √ | ' ' |  |
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

## 规则列表（规则引擎）-主表 t_plm_egn_policy

- **表名称：** 规则列表（规则引擎）-主表
- **表名：** t_plm_egn_policy

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fenablelist | fenablelist | bpchar | 1 |  | √ | ' ' |  |
| 3 | forgparam | forgparam | varchar | 50 |  | √ | ' ' |  |
| 4 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 5 | fbizappid | fbizappid | varchar | 18 |  | √ | ' ' |  |
| 6 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 7 | fstatus | fstatus | varchar | 50 |  | √ | 'C' |  |
| 8 | fcreatebuid | fcreatebuid | int8 | 64 |  | √ | 0 |  |
| 9 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 10 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 11 | fsceneid | fsceneid | int8 | 64 |  | √ | 0 |  |
| 12 | fenablecombo | fenablecombo | varchar | 50 |  | √ | ' ' |  |
| 13 | fissyspreset | fissyspreset | bpchar | 1 |  | √ | '0' |  |
| 14 | fruledate | fruledate | timestamp | 0 |  |  | null |  |
| 15 | fpolicymode | fpolicymode | varchar | 20 |  | √ | ' ' |  |
| 16 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 17 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 18 | fenableminfirst | fenableminfirst | bpchar | 1 |  | √ | ' ' |  |
| 19 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 20 | findex | findex | int4 | 32 |  | √ | 0 |  |
| 21 | fdisablerid | fdisablerid | int8 | 64 |  | √ | 0 |  |
| 22 | frosterresult | frosterresult | text | 0 |  |  | null |  |
| 23 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 24 | fretrundefault | fretrundefault | bpchar | 1 |  | √ | ' ' |  |
| 25 | frulesize | frulesize | varchar | 50 |  | √ | ' ' |  |
| 26 | fpolicy | 策略 | int8 | 64 |  | √ | 0 | [策略管理 plm_rengine_policy](../plmsm_files/plm_rengine_policy.md) |
| 27 | fresults | fresults | text | 0 |  |  | null |  |
| 28 | fsimplename | fsimplename | varchar | 100 |  | √ | ' ' |  |
| 29 | fenable | fenable | varchar | 2 |  | √ | '1' |  |
| 30 | fnumber | fnumber | varchar | 50 |  | √ | ' ' |  |
| 31 | fpolicytype | fpolicytype | varchar | 20 |  | √ | ' ' |  |
| 32 | frostercondition | frostercondition | text | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_egn_policy |  | fid |
| 2 | idx_plm_policy_bas |  | fsceneid,fbizappid |

---

## 规则信息分录-子表 t_plm_egn_drlfilter

- **表名称：** 规则信息分录-子表
- **表名：** t_plm_egn_drlfilter

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftemplatenumber | 模板编码 | varchar | 100 |  | √ | ' ' | 模板编码 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 5 | frulescene | frulescene | int8 | 64 |  | √ | 0 |  |
| 6 | ffilterresult | ffilterresult | text | 0 |  |  | ' ' |  |
| 7 | fbizappid | 所属应用 | varchar | 18 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 8 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 9 | fstatus | fstatus | varchar | 2 |  | √ | 'C' |  |
| 10 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 11 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 12 | fsceneid | 所属场景 | int8 | 64 |  | √ | 0 | [场景管理 plm_rengine_scene](../plmsm_files/plm_rengine_scene.md) |
| 13 | fruledescription | fruledescription | varchar | 255 |  | √ | ' ' |  |
| 14 | fissyspreset | fissyspreset | bpchar | 1 |  | √ | '0' |  |
| 15 | fruleorder | 优先级 | int8 | 64 |  | √ | 0 | 优先级 |
| 16 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 17 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 18 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 19 | fruleenable | fruleenable | bpchar | 1 |  | √ | '1' |  |
| 20 | fdisablerid | fdisablerid | int8 | 64 |  | √ | 0 |  |
| 21 | fdescription | 规则描述 | varchar | 255 |  | √ | ' ' | 规则描述 |
| 22 | frulenumber | 规则编码 | varchar | 50 |  | √ | ' ' | 规则编码 |
| 23 | fresultpreview | 结果 | varchar | 50 |  | √ | ' ' | 结果 |
| 24 | fresults | 结果 | text | 0 |  |  | null | 结果 |
| 25 | fsimplename | fsimplename | varchar | 100 |  | √ | ' ' |  |
| 26 | fenable | 使用状态 | varchar | 2 |  | √ | '1' | 使用状态 |
| 27 | fconditionpreview | 条件 | varchar | 50 |  | √ | ' ' | 条件 |
| 28 | frulebizapp | frulebizapp | varchar | 36 |  | √ | ' ' |  |
| 29 | fnumber | fnumber | varchar | 50 |  | √ | ' ' |  |
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
