# 风险评价-tctrc_risk_evaluation_new

## 风险评价-多语言表 t_tctrc_new_evaluation_l

- **表名称：** 风险评价-多语言表
- **表名：** t_tctrc_new_evaluation_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctrc_new_evaluation_l |  | fpkid |
| 2 | idx_tctrc_new_evaluation_l_0 |  | fid,flocaleid |

---

## 风险评价-主表 t_tctrc_new_evaluation

- **表名称：** 风险评价-主表
- **表名：** t_tctrc_new_evaluation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | friskresultfid | 风险结果主键 | varchar | 50 |  | √ | ' ' | 风险结果主键 |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fevaluation | 评价 | varchar | 50 |  | √ | ' ' | 评价,枚举: 0 :很棒 1 :一般 |
| 8 | forgld | forgld | int8 | 64 |  | √ | 0 |  |
| 9 | friskcode | 风险编号 | int8 | 64 |  | √ | 0 | [风险设置 tctrc_risk_definition](../tctrc_files/tctrc_risk_definition.md) |
| 10 | fprocesscontent | 处理说明 | varchar | 1000 |  | √ | ' ' | 处理说明 |
| 11 | friskname | 风险名称 | varchar | 300 |  | √ | ' ' | 风险名称 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fdealingrid | 处理人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | feedback | 意见反馈 | varchar | 1000 |  | √ | ' ' | 意见反馈 |
| 15 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 18 | fprocessstate | 处理状态 | varchar | 50 |  | √ | ' ' | 处理状态,枚举: 0 :无需处理 1 :待处理 2 :已处理 |
| 19 | fdealdate | 处理时间 | timestamp | 0 |  |  | null | 处理时间 |
| 20 | fprocessresult | 处理结果 | varchar | 50 |  | √ | ' ' | 处理结果,枚举: 0 :已采纳 1 :未采纳 |
| 21 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 0 :风险结果详情界面右侧 1 :风险处理弹窗 2 :新增风险评价 3 :运行清单界面 4 :风险设置 |
| 22 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fnumber | 编号 | varchar | 30 |  | √ | ' ' | 编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_newwval_num |  | friskcode |
| 2 | pk_tctrc_new_evaluation |  | fid |
