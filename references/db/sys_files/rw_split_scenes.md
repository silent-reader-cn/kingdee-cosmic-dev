# 读写分离场景配置-rw_split_scenes

## 读写分离场景配置-多语言表 t_rw_split_scenes_l

- **表名称：** 读写分离场景配置-多语言表
- **表名：** t_rw_split_scenes_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 场景 | varchar | 500 |  | √ | ' ' | 场景 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_rw_split_scenes_l |  | fpkid |
| 2 | idx_t_rw_split_scenes_l_fname |  | fname |
| 3 | idx_t_rw_split_scenes_l_fid |  | fid |

---

## 读写分离场景配置-主表 t_rw_split_scenes

- **表名称：** 读写分离场景配置-主表
- **表名：** t_rw_split_scenes

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 场景 | varchar | 500 |  | √ | ' ' | 场景 |
| 4 | fcurrent_config | 当前配置 | varchar | 50 |  | √ | ' ' | 当前配置,枚举: master_first :优先主库 slave_first :优先从库 |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | frelease_config | 已发布配置 | varchar | 50 |  | √ | ' ' | 已发布配置,枚举: master_first :优先主库 slave_first :优先从库 |
| 9 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 10 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 11 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_rw_split_scenes |  | fid |
| 2 | idx_rw_split_scenes_fbillno |  | fbillno |
