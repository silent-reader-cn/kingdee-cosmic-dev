# 基础资料运行时测试-ut_base_runtime

## 基础资料运行时测试-主表 t_ut_base_runtime

- **表名称：** 基础资料运行时测试-主表
- **表名：** t_ut_base_runtime

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 数据状态 | varchar | 30 |  |  | null | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 6 | fenable | 使用状态 | varchar | 30 |  |  | null | 使用状态,枚举: 0 :禁用 1 :可用 |
| 7 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ut_base_runtime_fnumber |  | fnumber |
| 2 | t_ut_base_runtime_pkey |  | fid |

---

## 基础资料运行时测试-多语言表 t_ut_base_runtime_l

- **表名称：** 基础资料运行时测试-多语言表
- **表名：** t_ut_base_runtime_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  |  | null | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ut_base_runtime_l_pkey |  | fpkid |
| 2 | idx_ut_base_runtime_l_fid |  | fid,flocaleid |
