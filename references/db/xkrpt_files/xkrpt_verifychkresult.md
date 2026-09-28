# 勾稽关系检查结果-xkrpt_verifychkresult

## 单据体-子表 t_xkrpt_formulacalresult

- **表名称：** 单据体-子表
- **表名：** t_xkrpt_formulacalresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcallresultex | 左表达式计算异常 | bpchar | 1 |  | √ | ' ' | 左表达式计算异常 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fcalrresultex | 右表达式计算异常 | bpchar | 1 |  | √ | ' ' | 右表达式计算异常 |
| 5 | fleftexpr | 左表达式 | varchar | 255 |  | √ | ' ' | 左表达式 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | frightexpr | 右表达式 | varchar | 255 |  | √ | ' ' | 右表达式 |
| 8 | fbinaryop | 双目运算符 | bpchar | 1 |  | √ | ' ' | 双目运算符,枚举: 0 := 1 : 4 :>= 5 :<> |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkrpt_formulacalresult |  | fentryid |
| 2 | idx_xkrpt_formulacalresult_id |  | fid |

---

## 勾稽关系检查结果-主表 t_xkrpt_verifyresult

- **表名称：** 勾稽关系检查结果-主表
- **表名：** t_xkrpt_verifyresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fmessage | 提示语 | varchar | 255 |  | √ | ' ' | 提示语 |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fsheetname | 表页名称 | varchar | 255 |  | √ | ' ' | 表页名称 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fscopetype | 合并方案 | int8 | 64 |  | √ | 0 | 合并方案 xkcr_scopetype |
| 8 | freportbase | 报表基础 | varchar | 36 |  | √ | ' ' | 报表(基础) xkrpt_reportbase |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fchecktype | 报表检查类型 | bpchar | 1 |  | √ | ' ' | 报表检查类型,枚举: 0 :表内勾稽检查 1 :项目勾稽检查 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fcheckresult | 检查结果 | bpchar | 1 |  | √ | ' ' | 检查结果,枚举: 0 :不通过 1 :通过 |
| 14 | fitemrelation | 项目勾稽关系 | int8 | 64 |  | √ | 0 | 项目勾稽关系 xkrpt_itemrelation |
| 15 | fverification | 表内检查公式 | int8 | 64 |  | √ | 0 | 表内检查公式 xkrpt_verification |
| 16 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkrpt_verifyresult_rpt |  | freportbase |
| 2 | pk_xkrpt_verifyresult |  | fid |

---

## 勾稽关系检查结果-多语言表 t_xkrpt_verifyresult_l

- **表名称：** 勾稽关系检查结果-多语言表
- **表名：** t_xkrpt_verifyresult_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmessage | 提示语 | varchar | 255 |  | √ | ' ' | 提示语 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkrpt_verifyresult_l |  | fid,flocaleid |
| 2 | pk_xkrpt_verifyresult_l |  | fpkid |
