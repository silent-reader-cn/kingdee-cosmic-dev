# 按信用分数升降级-task_creditbyscore

## 按信用分数升降级-主表 t_tk_creditbyscore

- **表名称：** 按信用分数升降级-主表
- **表名：** t_tk_creditbyscore

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fsubscorelimit | 每单最高减分： | numeric | 4 | 1 | √ | 0.0 | 每单最高减分： |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 9 | faddscore | 每单新增分数： | numeric | 4 | 1 | √ | 0.0 | 每单新增分数： |
| 10 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | key_1 |  | fnumber |
| 2 | t_tk_creditbyscore_pkey |  | fid |

---

## 按信用分数升降级-多语言表 t_tk_creditbyscore_l

- **表名称：** 按信用分数升降级-多语言表
- **表名：** t_tk_creditbyscore_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tk_creditbyscore_l_pkey |  | fpkid |
| 2 | index_ssc_creditbyscore_l_fid |  | fid,flocaleid |

---

## 单据体-子表 t_tk_creditbyscoreentry

- **表名称：** 单据体-子表
- **表名：** t_tk_creditbyscoreentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freducereason | 减分原因 | int8 | 64 |  | √ | 0 | 批退原因 task_withdrawal |
| 3 | freducetype | 减分类型 | varchar | 30 |  | √ | ' ' | 减分类型,枚举: task_withdrawal :共享审核批退原因 task_checkingpoint :质检任务不合格点 |
| 4 | freducescore | 减分数 | numeric | 4 | 1 | √ | 0.0 | 减分数 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tk_creditbyscoreentry_pkey |  | fentryid |
| 2 | t_tk_creditbyscoreentry_id |  | fid |
