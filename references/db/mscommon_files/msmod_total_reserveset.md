# 总量预留设置-msmod_total_reserveset

## 关联设置-子表 t_msmod_aggregateentry

- **表名称：** 关联设置-子表
- **表名：** t_msmod_aggregateentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frelateditem | 关联项 | varchar | 50 |  | √ | ' ' | 关联项,枚举: showreport :即时库存报表 showinvqty :显示可用库存服务 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | ftotalaggqty | 统计总量预留数量 | bpchar | 1 |  | √ | ' ' | 统计总量预留数量 |
| 5 | fcontrolevel | 控制级别 | varchar | 50 |  | √ | ' ' | 控制级别,枚举: strongcon :强控 weakcon :弱控 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msmod_aggregateentry |  | fentryid |
| 2 | idx_msmod_aggregateentry_fid |  | fid |

---

## 总量预留设置-多语言表 t_msmod_aggregatecfg_l

- **表名称：** 总量预留设置-多语言表
- **表名：** t_msmod_aggregatecfg_l

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
| 1 | idx_t_msmod_aggregatecfg_l_id |  | fid,flocaleid |
| 2 | pk_t_msmod_aggregatecfg_l |  | fpkid |

---

## 总量预留设置-主表 t_msmod_aggregatecfg

- **表名称：** 总量预留设置-主表
- **表名：** t_msmod_aggregatecfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fstaticfield | 不可更改维度 | varchar | 2000 |  | √ | ' ' | 不可更改维度 |
| 6 | fdim | 总量预留维度 | varchar | 2000 |  | √ | ' ' | 总量预留维度,枚举: |
| 7 | fisinit | 初始化状态 | varchar | 50 |  | √ | ' ' | 初始化状态,枚举: 0 :未初始化 1 :预留数量已初始化 2 :库存数量已初始化 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fisenable | 启用 | bpchar | 1 |  | √ | '0' | 启用 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fcompatibledetail | 兼容明细预留 | bpchar | 1 |  | √ | '0' | 兼容明细预留 |
| 14 | fenable | 使用状态 | varchar | 50 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msmod_aggregatecfg |  | fid |
