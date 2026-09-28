# 工单和组件清单字段映射-mpdm_ordertostock

## 单据体-子表 t_mpdm_otsentry

- **表名称：** 单据体-子表
- **表名：** t_mpdm_otsentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentityname | 实体 | varchar | 30 |  | √ | ' ' | 实体,枚举: A :单据头 B :单据体 |
| 3 | fentityident | 实体标识 | varchar | 50 |  | √ | ' ' | 实体标识 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_otsentry |  | fid,fseq |
| 2 | pk_mpdm_otsentry |  | fentryid |

---

## 工单和组件清单字段映射-主表 t_mpdm_ordertostock

- **表名称：** 工单和组件清单字段映射-主表
- **表名：** t_mpdm_ordertostock

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forder | 工单标识 | varchar | 50 |  | √ | ' ' | 工单标识 |
| 8 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 9 | fstock | 组件清单标识 | varchar | 50 |  | √ | ' ' | 组件清单标识 |
| 10 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_ordertostock |  | fnumber |
| 2 | pk_mpdm_ordertostock |  | fid |

---

## 子单据体-子表 t_mpdm_otsentryentity

- **表名称：** 子单据体-子表
- **表名：** t_mpdm_otsentryentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forderident | 工单字段标识 | varchar | 50 |  | √ | ' ' | 工单字段标识 |
| 2 | fordername | 工单字段名 | varchar | 50 |  | √ | ' ' | 工单字段名 |
| 3 | fstockident | 组件清单字段标识 | varchar | 50 |  | √ | ' ' | 组件清单字段标识 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 7 | fstockname | 组件清单字段名 | varchar | 50 |  | √ | ' ' | 组件清单字段名 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_otsentryentity |  | fdetailid |
| 2 | idx_mpdm_otsentryentity |  | fentryid,fseq |

---

## 工单和组件清单字段映射-多语言表 t_mpdm_ordertostock_l

- **表名称：** 工单和组件清单字段映射-多语言表
- **表名：** t_mpdm_ordertostock_l

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
| 1 | pk_mpdm_ordertostock_l |  | fpkid |
| 2 | idx_mpdm_ordertostock_l |  | fid,flocaleid |
