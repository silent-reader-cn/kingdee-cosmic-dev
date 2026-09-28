# 凭证摘要翻译记录-gl_ai_desctran_log

## 单据体-子表 t_gl_ai_desctran_logentry

- **表名称：** 单据体-子表
- **表名：** t_gl_ai_desctran_logentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fvoucherid | 凭证号 | int8 | 64 |  | √ | 0 | 凭证 gl_voucher |
| 3 | fsourcelanguageid | 当前语言 | int8 | 64 |  | √ | 0 | [语言种类 inte_language](../base_files/inte_language.md) |
| 4 | ftargetlanguageid | 目标语言 | int8 | 64 |  | √ | 0 | [语言种类 inte_language](../base_files/inte_language.md) |
| 5 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 6 | fexecuteresult | 执行状态 | bpchar | 1 |  | √ | '0' | 执行状态,枚举: 0 :失败 1 :成功 2 :部分失败 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | ffailreason | 失败原因 | varchar | 255 |  | √ | ' ' | 失败原因 |
| 9 | fbookid | 账簿 | int8 | 64 |  | √ | 0 | [账簿 gl_accountbook](../gl_files/gl_accountbook.md) |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fvouchertypeid | 凭证字 | int8 | 64 |  | √ | 0 | [凭证字 gl_vouchertype](../gl_files/gl_vouchertype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_desctrans_logentryfid |  | fid |
| 2 | pk_t_gl_ai_desctran_logentry |  | fentryid |

---

## 凭证摘要翻译记录-主表 t_gl_ai_desctran_log

- **表名称：** 凭证摘要翻译记录-主表
- **表名：** t_gl_ai_desctran_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexecutemethod | 触发方式 | bpchar | 1 |  | √ | '0' | 触发方式,枚举: 0 :定时翻译 1 :手工翻译 |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fscheduleschemeid | 定时方案 | int8 | 64 |  | √ | 0 | [凭证摘要定时翻译方案 gl_ai_desctran_schedule](../gl_files/gl_ai_desctran_schedule.md) |
| 5 | fexecutetime | 执行时间 | timestamp | 0 |  |  | null | 执行时间 |
| 6 | fnumber | 记录编号 | varchar | 30 |  | √ | ' ' | 记录编号 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_transdesc_logscheme_id |  | fscheduleschemeid |
| 2 | pk_t_gl_ai_desctran_log |  | fid |
