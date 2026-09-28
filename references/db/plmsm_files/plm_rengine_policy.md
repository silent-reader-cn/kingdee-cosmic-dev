# 策略管理-plm_rengine_policy

## 业务单元分录-子表 t_plm_rengine_policyscope

- **表名称：** 业务单元分录-子表
- **表名：** t_plm_rengine_policyscope

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcontainssub | 包含下级 | bpchar | 1 |  | √ | '0' | 包含下级 |
| 3 | fentitybuid | 组织基础资料 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plm_rengine_policyscope |  | fentryid |
| 2 | idx_plm_rengine_policyscope |  | fid,fentitybuid |

---

## 规则信息分录-多语言表 t_plm_egn_drlfilter_l

- **表名称：** 规则信息分录-多语言表
- **表名：** t_plm_egn_drlfilter_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 2 | fsimplename | fsimplename | varchar | 100 |  | √ | ' ' |  |
| 3 | fruledescription | 规则描述 | varchar | 255 |  | √ | ' ' | 规则描述 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
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

## 策略管理-主表 t_plm_egn_policy

- **表名称：** 策略管理-主表
- **表名：** t_plm_egn_policy

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fenablelist | 启用特殊名单 | bpchar | 1 |  | √ | ' ' | 启用特殊名单 |
| 3 | forgparam | 行政组织参数 | varchar | 50 |  | √ | ' ' | 行政组织参数,枚举: |
| 4 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 5 | fbizappid | 所属应用 | varchar | 18 |  | √ | ' ' | [业务应用实体（规则引擎） plm_rengine_bizapp](../plmsm_files/plm_rengine_bizapp.md) |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 50 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatebuid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fsceneid | 所属场景 | int8 | 64 |  | √ | 0 | [场景管理 plm_rengine_scene](../plmsm_files/plm_rengine_scene.md) |
| 12 | fenablecombo | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 1 :可用 0 :禁用 10 :待启用 |
| 13 | fissyspreset | 是否系统预置 | bpchar | 1 |  | √ | '0' | 是否系统预置 |
| 14 | fruledate | 用来触发日期操作（勿删） | timestamp | 0 |  |  | null | 用来触发日期操作（勿删） |
| 15 | fpolicymode | 策略模式 | varchar | 20 |  | √ | ' ' | 策略模式,枚举: FirstMatch :首次匹配 FullMatch :全量匹配 |
| 16 | fname | 策略名称 | varchar | 100 |  | √ | ' ' | 策略名称 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fenableminfirst | 启用组织明细优先 | bpchar | 1 |  | √ | ' ' | 启用组织明细优先 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | findex | 排序号 | int4 | 32 |  | √ | 0 | 排序号 |
| 21 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | frosterresult | 特殊名单结果 | text | 0 |  |  | null | 特殊名单结果 |
| 23 | fdescription | 策略描述 | varchar | 255 |  | √ | ' ' | 策略描述 |
| 24 | fretrundefault | 返回默认结果 | bpchar | 1 |  | √ | ' ' | 返回默认结果 |
| 25 | frulesize | 规则 | varchar | 50 |  | √ | ' ' | 规则 |
| 26 | fpolicy | fpolicy | int8 | 64 |  | √ | 0 |  |
| 27 | fresults | 默认返回结果 | text | 0 |  |  | null | 默认返回结果 |
| 28 | fsimplename | 简称 | varchar | 100 |  | √ | ' ' | 简称 |
| 29 | fenable | 使用状态 | varchar | 2 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 10 :待启用 |
| 30 | fnumber | 策略编码 | varchar | 50 |  | √ | ' ' | 策略编码 |
| 31 | fpolicytype | 策略分类 | varchar | 20 |  | √ | ' ' | 策略分类,枚举: decision_set :决策集 decision_table :决策表 |
| 32 | frostercondition | 特殊名单条件 | text | 0 |  |  | null | 特殊名单条件 |

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

## 策略管理-多语言表 t_plm_egn_policy_l

- **表名称：** 策略管理-多语言表
- **表名：** t_plm_egn_policy_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 策略名称 | varchar | 100 |  | √ | ' ' | 策略名称 |
| 3 | fsimplename | 简称 | varchar | 100 |  | √ | ' ' | 简称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fdescription | 策略描述 | varchar | 255 |  | √ | ' ' | 策略描述 |
| 6 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_egn_policy_l |  | fpkid |
| 2 | idx_plm_policy_l |  | fid,flocaleid |

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
| 13 | fruledescription | 规则描述 | varchar | 255 |  | √ | ' ' | 规则描述 |
| 14 | fissyspreset | fissyspreset | bpchar | 1 |  | √ | '0' |  |
| 15 | fruleorder | 优先级 | int8 | 64 |  | √ | 0 | 优先级 |
| 16 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 17 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 18 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 19 | fruleenable | fruleenable | bpchar | 1 |  | √ | '1' |  |
| 20 | fdisablerid | fdisablerid | int8 | 64 |  | √ | 0 |  |
| 21 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
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
