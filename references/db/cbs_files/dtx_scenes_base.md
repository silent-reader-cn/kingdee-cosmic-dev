# 场景基础资料-dtx_scenes_base

## 场景基础资料-多语言表 t_cbs_dtx_tx_scenes_l

- **表名称：** 场景基础资料-多语言表
- **表名：** t_cbs_dtx_tx_scenes_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | fremark | varchar | 500 |  | √ | ' ' |  |
| 3 | fname | 场景名称 | varchar | 255 |  | √ | ' ' | 场景名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbs_dtx_tx_scenes_l_0 |  | fid,flocaleid |
| 2 | pk_t_cbs_dtx_tx_scenes_l |  | fpkid |

---

## 场景基础资料-主表 t_cbs_dtx_tx_scenes

- **表名称：** 场景基础资料-主表
- **表名：** t_cbs_dtx_tx_scenes

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | fremark | varchar | 500 |  |  | ' ' |  |
| 3 | fname | 场景名称 | varchar | 255 |  | √ | ' ' | 场景名称 |
| 4 | fphone | fphone | varchar | 240 |  | √ | ' ' |  |
| 5 | fnotice_operator | fnotice_operator | bpchar | 1 |  | √ | '0' |  |
| 6 | fapp | fapp | varchar | 100 |  | √ | ' ' |  |
| 7 | falarm_type | falarm_type | varchar | 200 |  | √ | ' ' |  |
| 8 | froutekey | froutekey | varchar | 50 |  |  | ' ' |  |
| 9 | fcode | 场景编码 | varchar | 100 |  | √ | ' ' | 场景编码 |
| 10 | fbusiness_type | fbusiness_type | varchar | 100 |  |  | ' ' |  |
| 11 | fappid | fappid | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbs_dtx_tx_scenes |  | fcode |
| 2 | pk_t_cbs_dtx_tx_scenes |  | fid |
