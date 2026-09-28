# 智能订货-暂存单-ocdma_aiordersession

## 智能订货-暂存单-主表 t_ocdma_aiordersession

- **表名称：** 智能订货-暂存单-主表
- **表名：** t_ocdma_aiordersession

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fauthorize | 供货关系 | int8 | 64 |  | √ | 0 | [供货关系 ocdbd_channel_authorize](../ocdbd_files/ocdbd_channel_authorize.md) |
| 3 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fchatsessionid | chatsessionid | varchar | 50 |  | √ | ' ' | chatsessionid |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdma_aiordersession_sid |  | fchatsessionid |
| 2 | idx_ocdma_aiordersession_time |  | fmodifytime |
| 3 | pk_ocdma_aiordersession |  | fid |

---

## 单据体-子表 t_ocdma_aiordersession_e

- **表名称：** 单据体-子表
- **表名：** t_ocdma_aiordersession_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 订购数量 | numeric | 23 | 10 | √ | 0 | 订购数量 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fnumber | 查询的内容 | varchar | 50 |  | √ | ' ' | 查询的内容 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fitemid | 查询到的商品 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdma_aiordersession_e_fd |  | fid |
| 2 | pk_ocdma_aiordersession_e |  | fentryid |
