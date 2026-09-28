# 数据处理任务节点-pbd_scdatatask

## 数据处理任务节点-多语言表 t_pur_datahandletask_l

- **表名称：** 数据处理任务节点-多语言表
- **表名：** t_pur_datahandletask_l

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
| 1 | pk_pur_datahandletask_l |  | fpkid |
| 2 | idx_pur_datahandletask_l_fid |  | fid,flocaleid |

---

## 数据处理任务节点-主表 t_pur_datahandletask

- **表名称：** 数据处理任务节点-主表
- **表名：** t_pur_datahandletask

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fparam | 参数 | varchar | 255 |  | √ | ' ' | 参数 |
| 4 | fgroupid | fgroupid | int8 | 64 |  | √ | 0 |  |
| 5 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 6 | fcanskip | 失败时可跳过 | bpchar | 1 |  | √ | '0' | 失败时可跳过 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fclassname | 执行类 | varchar | 255 |  | √ | ' ' | 执行类 |
| 9 | fcandisable | 可禁用 | bpchar | 1 |  | √ | '1' | 可禁用 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fisdisplay | 是否展示进度 | bpchar | 1 |  | √ | '1' | 是否展示进度 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fispre | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 16 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pur_datahandletask |  | fid |
| 2 | idx_pur_datahandletask_fnumber |  | fnumber |
