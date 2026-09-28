# 合法性检查结果明细-cad_calccheckresult

## 合法性检查结果明细-主表 t_cad_calccheckresult

- **表名称：** 合法性检查结果明细-主表
- **表名：** t_cad_calccheckresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcalctime | 计算日期 | timestamp | 0 |  |  | null | 计算日期 |
| 3 | fcnsmtime | 耗时 | int8 | 64 |  | √ | 0 | 耗时 |
| 4 | fcosttypeid | 标准成本方案 | int8 | 64 |  | √ | 0 | 标准成本方案 cad_costtype |
| 5 | fcheckresult | 检查结果 | varchar | 30 |  | √ | ' ' | 检查结果,枚举: 0 :通过 1 :提醒 2 :不通过 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fcheckitemid | 检查项 | int8 | 64 |  | √ | 0 | 合法性检查项 cad_checkitem |
| 8 | fmainorgid | 主业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fcalctaskrecordid | 执行任务记录 | int8 | 64 |  | √ | 0 | 标准成本任务 sco_task |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_cad_calccheckresult_df |  | fcosttypeid,fcalctaskrecordid,fcreatetime |
| 2 | t_cad_calccheckresult_pkey |  | fid |

---

## 合法性检查结果明细-多语言表 t_cad_calccheckresult_l

- **表名称：** 合法性检查结果明细-多语言表
- **表名：** t_cad_calccheckresult_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 4 | fcheckresultdesc | 结果描述 | varchar | 255 |  | √ | ' ' | 结果描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_cad_calccheckrs_l_id |  | fid,flocaleid |
| 2 | t_cad_calccheckresult_l_pkey |  | fpkid |

---

## 合法性检查结果明细-子表 t_cad_calccheckdtresult

- **表名称：** 合法性检查结果明细-子表
- **表名：** t_cad_calccheckdtresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpageid | 页面ID | varchar | 100 |  | √ | ' ' | 页面ID |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fsuggest | 操作建议 | varchar | 100 |  | √ | ' ' | 操作建议 |
| 5 | fbizid | 业务ID | varchar | 100 |  | √ | ' ' | 业务ID |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | ferrordesc | 检查明细 | varchar | 2000 |  | √ | ' ' | 检查明细 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cad_calccheckdtresult_pkey |  | fentryid |
| 2 | index_cad_calccheckrsdt_df |  | fid,fseq |
