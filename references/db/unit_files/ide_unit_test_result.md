# 单元测试结果-ide_unit_test_result

## 单元测试结果-主表 t_bas_unittestresult

- **表名称：** 单元测试结果-主表
- **表名：** t_bas_unittestresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 18 |  | √ | ' ' | id |
| 2 | fsubsysid | 所属应用 | varchar | 32 |  |  | null | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 3 | fresulttype | 是否正常 | bpchar | 1 |  |  | null | 是否正常 |
| 4 | ftestnumber | 用例项数量 | int8 | 64 |  |  | null | 用例项数量 |
| 5 | fcaseid | 测试用例名称 | varchar | 18 |  |  | null | [单元测试功能发布 ide_unit_test_detail](../unit_files/ide_unit_test_detail.md) |
| 6 | fdatetime | 时间 | timestamp | 0 |  |  | null | 时间 |
| 7 | freturnmsg | 测试结果 | varchar | 100 |  |  | null | 测试结果 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bas_unittestresult_pkey |  | fid |
| 2 | idx_bas_unittestresult_fcaseid |  | fcaseid |

---

## 单据体-子表 t_bas_unitestresultdetail

- **表名称：** 单据体-子表
- **表名：** t_bas_unitestresultdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 18 |  | √ | ' ' |  |
| 2 | ffuncname | 函数名称 | varchar | 200 |  | √ | ' ' | 函数名称 |
| 3 | fstartdatetime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 4 | fenddatetime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 5 | fconsume | 耗时(ms） | int8 | 64 |  |  | null | 耗时(ms） |
| 6 | fseq | 分录行号 | int8 | 64 |  |  | null | 分录行号 |
| 7 | ftestresult | 测试详情 | text | 0 |  |  | null | 测试详情 |
| 8 | fentryid | fentryid | varchar | 18 |  | √ | ' ' | id |
| 9 | ffuncdescript | 函数描述 | varchar | 400 |  | √ | ' ' | 函数描述 |
| 10 | freturn | 是否成功 | bpchar | 1 |  |  | null | 是否成功 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bas_ut_resultdetail_fid |  | fid |
| 2 | t_bas_unitestresultdetail_pkey |  | fentryid |
