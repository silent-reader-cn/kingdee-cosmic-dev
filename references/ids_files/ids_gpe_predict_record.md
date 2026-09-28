# 预测结果-ids_gpe_predict_record

## 预测结果-主表 t_ids_gpe_predict_record

- **表名称：** 预测结果-主表
- **表名：** t_ids_gpe_predict_record

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fexecutestatus | 执行状态 | varchar | 10 |  | √ | ' ' | 执行状态,枚举: 0 :等待执行 10 :执行中 20 :执行成功 30 :执行失败 |
| 6 | ffailmsg | 失败原因 | varchar | 255 |  | √ | ' ' | 失败原因 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | ffailmsg_tag | 失败原因_详情 | text | 0 |  |  | null | 失败原因_详情 |
| 9 | ftimecomsuming | 耗时 | varchar | 50 |  | √ | ' ' | 耗时 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fscheme | 预测模型方案 | int8 | 64 |  | √ | 0 | 预测模型方案 ids_gpe_scheme |
| 14 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 16 | frequestid | 执行预测请求ID | varchar | 50 |  | √ | ' ' | 执行预测请求ID |
| 17 | fendtime | 执行结束时间 | timestamp | 0 |  |  | null | 执行结束时间 |
| 18 | fattachmentid | 附件 | int8 | 64 |  | √ | 0 | 附件 ids_gpe_attachment |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ids_gpe_predict_record |  | fid |
| 2 | idx_ids_gpe_pred_record_number |  | fnumber |

---

## 预测结果-多语言表 t_ids_gpe_predict_record_l

- **表名称：** 预测结果-多语言表
- **表名：** t_ids_gpe_predict_record_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ids_gpe_record_l_fname |  | fname |
| 2 | pk_t_ids_gpe_predict_record_l |  | fpkid |
