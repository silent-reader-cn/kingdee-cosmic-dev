# 横道类型-msplan_gantt_crosstype

## 横道类型-主表 t_msplan_crosstype

- **表名称：** 横道类型-主表
- **表名：** t_msplan_crosstype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 横道类型名称 | varchar | 50 |  | √ | ' ' | 横道类型名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fcrosstype | 横道类型 | varchar | 5 |  | √ | ' ' | 横道类型,枚举: 1 :当前横道 2 :完成百分比横道 3 :计划横道 4 :实际横道 5 :尚需横道 6 :目标横道 |
| 7 | fcrossobj | 横道对象 | varchar | 5 |  | √ | ' ' | 横道对象,枚举: 1 :任务横道 2 :里程碑横道 3 :关键路径横道 4 :汇总横道 5 :空闲横道 6 :二级关键路径横道 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fenable | 使用状态 | varchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fnumber | 横道类型编码 | varchar | 30 |  | √ | ' ' | 横道类型编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_msplan_crosstype |  | fid |
| 2 | idx_msplan_crospe_fcreatetime |  | fcreatetime |
| 3 | idx_msplan_crospe_fnumber |  | fnumber |

---

## 横道类型-多语言表 t_msplan_crosstype_l

- **表名称：** 横道类型-多语言表
- **表名：** t_msplan_crosstype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 横道类型名称 | varchar | 50 |  | √ | ' ' | 横道类型名称 |
| 3 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msplan_crospel_fid |  | fid,flocaleid |
| 2 | idx_msplan_crospel_fname |  | fname |
| 3 | pk_msplan_crosstype_l |  | fpkid |
