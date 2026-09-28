# 专家考评结果-src_evaluateresult

## 专家考评结果-主表 t_src_evaluateresulthead

- **表名称：** 专家考评结果-主表
- **表名：** t_src_evaluateresulthead

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
| 1 | pk_src_evaluateresulthead |  | fid |
| 2 | idx_src_evaluateresulthead_pid |  | fparentid |

---

## 资审结果分录-子表 t_src_evaluateresult

- **表名称：** 资审结果分录-子表
- **表名：** t_src_evaluateresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fgradeid | 考评等级 | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 3 | finputscore | 考评得分(线下) | numeric | 23 | 10 | √ | 0 | 考评得分(线下) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fnote | 备注 | varchar | 100 |  | √ | ' ' | 备注 |
| 6 | faptitudenote | 考评意见 | varchar | 255 |  | √ | ' ' | 考评意见 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fscoretaskid | 考评记录 | int8 | 64 |  | √ | 0 | 考评记录F7 src_evaluatetaskf7 |
| 9 | fisaptitude | 考评结果 | bpchar | 1 |  | √ | '1' | 考评结果,枚举: 0 :未考评 1 :考评合格 2 :考评不合格 |
| 10 | fentryparentid | fentryparentid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_src_evaluateresult |  | fentryid |
| 2 | idx_src_evaluateresult_sid |  | fscoretaskid |
| 3 | idx_src_evaluateresult_fid |  | fid |
| 4 | idx_src_evaluateresult_pid |  | fentryparentid |
