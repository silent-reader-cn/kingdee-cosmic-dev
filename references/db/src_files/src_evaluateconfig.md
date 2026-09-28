# 专家考评设置-src_evaluateconfig

## 考评设置分录-子表 t_src_evaluateconfig

- **表名称：** 考评设置分录-子表
- **表名：** t_src_evaluateconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fagentid | 代理评委 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fgradeschemeid | 分级方案 | int8 | 64 |  | √ | 0 | 考评分级方案 src_expertgrade |
| 4 | fdateto | 评分结束时间 | timestamp | 0 |  |  | null | 评分结束时间 |
| 5 | fqfilter | 当前查询条件 | varchar | 255 |  | √ | ' ' | 当前查询条件 |
| 6 | fproschemeid | fproschemeid | int8 | 64 |  | √ | 0 |  |
| 7 | fentrystatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: A :待下达 B :已下达 |
| 8 | fschemeid | 考评方案 | int8 | 64 |  | √ | 0 | 方案配置 src_scheme |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 11 | fexpertcount | 评委最低人数 | int4 | 32 |  | √ | 0 | 评委最低人数 |
| 12 | fentryparentid | 父单据ID | int8 | 64 |  | √ | 0 | 父单据ID |
| 13 | findextypeid | 指标类型 | int8 | 64 |  | √ | 0 | 指标类型 src_indexclass |
| 14 | fqfilter_tag | 当前查询条件_详情 | text | 0 |  |  | null | 当前查询条件_详情 |
| 15 | fweight | 类型权重(%) | numeric | 19 | 6 | √ | 0 | 类型权重(%) |
| 16 | fpackageid | 标段名称 | int8 | 64 |  | √ | 0 | 标段名称 src_packagef7 |
| 17 | fdatefrom | 评分开始时间 | timestamp | 0 |  |  | null | 评分开始时间 |
| 18 | ftplname | 考评方案名称 | varchar | 100 |  | √ | ' ' | 考评方案名称 |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_evaluateconfig_pid |  | fentryparentid |
| 2 | pk_src_evaluateconfig |  | fentryid |
| 3 | idx_src_evaluateconfig_fid |  | fid |

---

## 考评方案(线下)-附件表 t_src_evaluateconfig_fj

- **表名称：** 考评方案(线下)-附件表
- **表名：** t_src_evaluateconfig_fj

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 附件字段实体 bd_attachment |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_evaluateconfig_bid |  | fbasedataid |
| 2 | idx_src_evaluateconfig_fj |  | fentryid |
| 3 | pk_src_evaluateconfig_fj |  | fpkid |

---

## 评委-多选基础资料表 t_src_evaluateuser

- **表名称：** 评委-多选基础资料表
- **表名：** t_src_evaluateuser

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_evaluateuser_fbid |  | fbasedataid |
| 2 | pk_src_evaluateuser |  | fpkid |
| 3 | idx_src_evaluateuser_fentryid |  | fentryid |

---

## 专家考评设置-主表 t_src_evaluateconfighead

- **表名称：** 专家考评设置-主表
- **表名：** t_src_evaluateconfighead

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forigin | 发起方 | bpchar | 1 |  | √ | ' ' | 发起方,枚举: 1 :采购方端 2 :供应商端 3 :两端公用 |
| 3 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 4 | fentitykey | 组件标识 | varchar | 50 |  | √ | ' ' | 组件标识 |
| 5 | fpentitykey | 父单据标识 | varchar | 50 |  | √ | ' ' | 父单据标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_evaluateconfighead_pid |  | fparentid |
| 2 | pk_src_evaluateconfighead |  | fid |
