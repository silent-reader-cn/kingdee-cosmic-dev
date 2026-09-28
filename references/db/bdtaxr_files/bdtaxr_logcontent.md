# 单据计税日志内容-bdtaxr_logcontent

## 单据计税日志内容-多语言表 t_bdtaxr_logcontent_l

- **表名称：** 单据计税日志内容-多语言表
- **表名：** t_bdtaxr_logcontent_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |

---

## 单据体-子表 t_bdtaxr_logdetail

- **表名称：** 单据体-子表
- **表名：** t_bdtaxr_logdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstep | 执行步骤 | varchar | 50 |  | √ | ' ' | 执行步骤 |
| 3 | fstepno | 步骤序号 | int4 | 32 |  | √ | 0 | 步骤序号 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | flogcontent | 日志内容 | varchar | 1500 |  | √ | ' ' | 日志内容 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bdtaxr_logdetail_fk |  | fid |
| 2 | pk_bdtaxr_logdetail |  | fentryid |

---

## 单据计税日志内容-主表 t_bdtaxr_logcontent

- **表名称：** 单据计税日志内容-主表
- **表名：** t_bdtaxr_logcontent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbusinesslog_tag | 业务日志_详情 | text | 0 |  |  | null | 业务日志_详情 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | ftaxcodelinelog | 后台日志 | varchar | 255 |  | √ | ' ' | 后台日志 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fbilltaxlog | 单据计税日志 | int8 | 64 |  | √ | 0 | 单据计税日志 bdtaxr_billtaxlog |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | flineresults | 分录行计税结果 | varchar | 50 |  | √ | ' ' | 分录行计税结果,枚举: succ :成功 fail :失败 |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fbusinesslog | 业务日志 | varchar | 255 |  | √ | ' ' | 业务日志 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | ftaxcodelinelog_tag | 后台日志_详情 | text | 0 |  |  | null | 后台日志_详情 |
| 15 | fnumber | 单据分录序号 | varchar | 34 |  | √ | ' ' | 单据分录序号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bdtaxr_logcontent |  | fnumber |
| 2 | pk_bdtaxr_logcontent |  | fid |
