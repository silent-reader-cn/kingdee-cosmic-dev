# 业务操作日志-tnd_bizoperatelog

## 供应商-废弃-多选基础资料表 t_pds_bizoperatelog_sup

- **表名称：** 供应商-废弃-多选基础资料表
- **表名：** t_pds_bizoperatelog_sup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_bizoperatelog_sup_fid |  | fid |
| 2 | pk_pds_bizoperatelog_sup |  | fpkid |
| 3 | idx_pds_bizoperatelog_sup_bid |  | fbasedataid |

---

## 业务操作日志-主表 t_pds_bizoperatelog

- **表名称：** 业务操作日志-主表
- **表名：** t_pds_bizoperatelog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fprojectid | 寻源项目 | int8 | 64 |  | √ | 0 | [招标项目F7 src_projectf7](../src_files/src_projectf7.md) |
| 3 | fcreatorid | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | freason1 | 备注 | varchar | 1024 |  | √ | ' ' | 备注 |
| 5 | fcreatetime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 6 | foptype | 操作类型 | varchar | 50 |  | √ | ' ' | 操作类型 |
| 7 | fopkey | 操作标识 | varchar | 50 |  | √ | ' ' | 操作标识 |
| 8 | fturns | 议价轮次 | varchar | 2 |  | √ | ' ' | 议价轮次,枚举: 1 :未议价 2 :议价(1) 3 :议价(2) 4 :议价(3) 5 :议价(4) 6 :议价(5) 7 :议价(6) 8 :议价(7) 9 :议价(8) 10 :议价(9) |
| 9 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 10 | fentitykey | 单据标识 | varchar | 50 |  | √ | ' ' | 单据标识 |
| 11 | fvieturns | 竞价轮次 | varchar | 2 |  | √ | ' ' | 竞价轮次,枚举: 1 :首轮 2 :竞价(2) 3 :竞价(3) 4 :竞价(4) 5 :竞价(5) 6 :竞价(6) 7 :竞价(7) 8 :竞价(8) 9 :竞价(9) |
| 12 | freason | 操作原因 | varchar | 1024 |  | √ | ' ' | 操作原因 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pds_bizoperatelog |  | fid |
| 2 | idx_pds_bizoperatelog_bid |  | fbillid |
| 3 | idx_pds_bizoperatelog_oid |  | foptype |
| 4 | idx_pds_bizoperatelog_pid |  | fprojectid |

---

## 业务人员-多选基础资料表 t_pds_bizoperatelog_user

- **表名称：** 业务人员-多选基础资料表
- **表名：** t_pds_bizoperatelog_user

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_bizoperatelog_user_bid |  | fbasedataid |
| 2 | pk_pds_bizoperatelog_user |  | fpkid |
| 3 | idx_pds_bizoperatelog_user_fid |  | fid |
