# 指标管理-plm_rengine_target

## 指标管理-多语言表 t_plm_egn_target_l

- **表名称：** 指标管理-多语言表
- **表名：** t_plm_egn_target_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 指标名称 | varchar | 100 |  | √ | ' ' | 指标名称 |
| 3 | fsimplename | 简称 | varchar | 100 |  | √ | ' ' | 简称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fdescription | 指标描述 | varchar | 255 |  | √ | ' ' | 指标描述 |
| 6 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_target_l |  | fid,flocaleid |
| 2 | pk_plm_egn_target_l |  | fpkid |

---

## 指标管理-主表 t_plm_egn_target

- **表名称：** 指标管理-主表
- **表名：** t_plm_egn_target

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fparam | 3、函数参数： | varchar | 255 |  | √ | ' ' | 3、函数参数： |
| 3 | ftemplatenumber | 模板编码 | varchar | 100 |  | √ | ' ' | 模板编码 |
| 4 | fformat | 2、函数格式： | varchar | 255 |  | √ | ' ' | 2、函数格式： |
| 5 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 6 | fbizappid | 所属应用 | varchar | 18 |  | √ | ' ' | [业务应用实体（规则引擎） plm_rengine_bizapp](../plmsm_files/plm_rengine_bizapp.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | ffuncdescription | 1、函数描述： | varchar | 255 |  | √ | ' ' | 1、函数描述： |
| 9 | fstatus | 数据状态 | varchar | 2 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fsceneid | 所属场景 | int8 | 64 |  | √ | 0 | [场景管理 plm_rengine_scene](../plmsm_files/plm_rengine_scene.md) |
| 13 | fexample | 4、举例： | varchar | 255 |  | √ | ' ' | 4、举例： |
| 14 | fdisplayfunctext | 表达式 | text | 0 |  |  | null | 表达式 |
| 15 | fissyspreset | 是否系统预置 | bpchar | 1 |  | √ | '0' | 是否系统预置 |
| 16 | fruledate | 用来触发日期操作的控件（勿删） | timestamp | 0 |  |  | null | 用来触发日期操作的控件（勿删） |
| 17 | ftargettype | 指标类型 | varchar | 50 |  | √ | ' ' | 指标类型,枚举: condition :条件指标 function :运算指标 |
| 18 | fbuid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | fname | 指标名称 | varchar | 100 |  | √ | ' ' | 指标名称 |
| 20 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fresultdate | 日期（勿删） | timestamp | 0 |  |  | null | 日期（勿删） |
| 22 | felses | 否则 | text | 0 |  |  | null | 否则 |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | findex | 排序号 | int8 | 64 |  | √ | 0 | 排序号 |
| 25 | fapplicationscope | 适用范围 | varchar | 20 |  | √ | ' ' | 适用范围,枚举: share :全局共享 private :私有 scopeshare :管控范围内共享 |
| 26 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 27 | fdescription | 指标描述 | varchar | 255 |  | √ | ' ' | 指标描述 |
| 28 | ftargetenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 1 :可用 0 :禁用 |
| 29 | fdateformat | 掩码 | varchar | 50 |  | √ | ' ' | 掩码,枚举: yyyy-MM-dd :YYYY-MM-DD yyyy/MM/dd :YYYY/MM/DD yy-MM/dd :YY-MM/DD yyyy-MM :YYYY-MM yyyy/MM :YYYY/MM yyyy :YYYY |
| 30 | freturntype | 返回类型 | varchar | 50 |  | √ | ' ' | 返回类型,枚举: string :文本 number :数值 date :日期 boolean :布尔 |
| 31 | felsedate1 | 日期（勿删） | timestamp | 0 |  |  | null | 日期（勿删） |
| 32 | fresults | 结果 | text | 0 |  |  | null | 结果 |
| 33 | fdatemat | fdatemat | varchar | 30 |  | √ | ' ' |  |
| 34 | freturnparamfield | 对象字段 | varchar | 100 |  | √ | ' ' | 对象字段,枚举: |
| 35 | fsimplename | 简称 | varchar | 100 |  | √ | ' ' | 简称 |
| 36 | fenable | 使用状态 | varchar | 2 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 10 :待启用 |
| 37 | fnumber | 指标编码 | varchar | 50 |  | √ | ' ' | 指标编码 |
| 38 | fconditions | 条件 | text | 0 |  |  | null | 条件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_egn_target |  | fid |
| 2 | idx_plm_target_bss |  | fsceneid |
