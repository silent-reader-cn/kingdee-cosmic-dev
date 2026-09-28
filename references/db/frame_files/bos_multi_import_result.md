# 导入结果-bos_multi_import_result

## 导入结果-主表 t_bas_mulimp_result

- **表名称：** 导入结果-主表
- **表名：** t_bas_mulimp_result

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatetime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 4 | fisdeleted | fisdeleted | bpchar | 1 |  | √ | ' ' |  |
| 5 | fmodifytime | 结束时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 结束时间 |
| 6 | fstatus | 单据状态 | bpchar | 1 |  | √ | 'C' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | ffailed | 失败总数 | int4 | 32 |  | √ | 0 | 失败总数 |
| 8 | fcreatorid | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fobjname | 业务对象 | varchar | 1000 |  | √ | ' ' | 业务对象 |
| 10 | fimportstatus | 导入状态 | bpchar | 1 |  | √ | ' ' | 导入状态,枚举: 0 :导入中 1 :导入完成 |
| 11 | furl | furl | varchar | 500 |  | √ | ' ' |  |
| 12 | fnumber | 日志编码 | varchar | 30 |  | √ | ' ' | 日志编码 |
| 13 | ftotal | 执行总数 | int4 | 32 |  | √ | 0 | 执行总数 |
| 14 | fusetime | 用时（秒） | int4 | 32 |  | √ | 0 | 用时（秒） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bas_mulimp_result |  | fid |
| 2 | idx_multi_imp_result_number |  | fnumber |

---

## 子单据体-子表 t_bas_mulimp_res_subtree

- **表名称：** 子单据体-子表
- **表名：** t_bas_mulimp_res_subtree

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ffailreason_tag | 失败原因_详情 | text | 0 |  |  | null | 失败原因_详情 |
| 2 | frow | 行数 | int4 | 32 |  | √ | 0 | 行数 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | ffailreason | 失败原因 | varchar | 100 |  | √ | ' ' | 失败原因 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bas_mulimp_res_subtree |  | fdetailid |
| 2 | idx_bas_mulimp_res_subtree_fk |  | fentryid |

---

## 实体详细错误信息-子表 t_bas_mulimp_resulttree

- **表名称：** 实体详细错误信息-子表
- **表名：** t_bas_mulimp_resulttree

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 目标实体 | varchar | 255 |  | √ | ' ' | 目标实体 |
| 3 | fentityimportstatus | fentityimportstatus | bpchar | 1 |  | √ | '0' |  |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | ffailedreason | ffailedreason | varchar | 255 |  | √ | ' ' |  |
| 6 | ffailednumber | 失败数量 | int4 | 32 |  | √ | 0 | 失败数量 |
| 7 | ffailedreason_tag | ffailedreason_tag | text | 0 |  |  | null |  |
| 8 | fdatareplacerulefield | 数据替换唯一值 | varchar | 500 |  | √ | ' ' | 数据替换唯一值 |
| 9 | fdatasheetname | 对应Excel工作表页签 | varchar | 100 |  | √ | ' ' | 对应Excel工作表页签 |
| 10 | fcontractfailednum | 关联字段不匹配未导入数据量 | int4 | 32 |  | √ | 0 | 关联字段不匹配未导入数据量 |
| 11 | fentrytotal | 导入数据量 | int4 | 32 |  | √ | 0 | 导入数据量 |
| 12 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | fimporttype | 导入方式 | bpchar | 1 |  | √ | '0' | 导入方式,枚举: 0 :新增导入 1 :更新导入 2 :新增并更新导入 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bas_mulimp_resulttree |  | fentryid |
| 2 | idx_multi_imp_resulttree_id |  | fid |
