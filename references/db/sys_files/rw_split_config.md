# 读写分离配置-rw_split_config

## 读写分离配置-主表 t_rw_split_config

- **表名称：** 读写分离配置-主表
- **表名：** t_rw_split_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fgroupid | 所属应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 4 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 5 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | frelease_config | 已发布配置 | varchar | 50 |  | √ | ' ' | 已发布配置,枚举: master_first :主库优先 slave_first :从库优先 |
| 8 | fpreset_data | 预置数据 | varchar | 50 |  | √ | ' ' | 预置数据,枚举: master_first :主库优先 slave_first :从库优先 delete :已删除 |
| 9 | fentity_no | 编码 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 10 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fcurrent_config | 配置 | varchar | 50 |  | √ | ' ' | 配置,枚举: master_first :主库优先 slave_first :从库优先 delete :已失效 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fpreset | 是否是预置数据 | int4 | 32 |  | √ | 0 | 是否是预置数据 |
| 15 | fscenes | 所属场景 | varchar | 50 |  | √ | ' ' | 所属场景,枚举: billlist :列表 report :报表 custom :自定义 |
| 16 | fbillno | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rw_split_config_fname |  | fname |
| 2 | pk_t_rw_split_config |  | fid |
| 3 | idx_rw_split_config_fbillno |  | fbillno |

---

## 读写分离配置-多语言表 t_rw_split_config_l

- **表名称：** 读写分离配置-多语言表
- **表名：** t_rw_split_config_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_rw_split_config_l_fid |  | fid |
| 2 | pk_t_rw_split_config_l |  | fpkid |
| 3 | idx_t_rw_split_config_l_fname |  | fname |
