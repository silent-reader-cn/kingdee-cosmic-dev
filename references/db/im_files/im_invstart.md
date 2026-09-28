# 启用库存-im_invstart

## 物料设置-子表 t_im_warehousesetup_mater

- **表名称：** 物料设置-子表
- **表名：** t_im_warehousesetup_mater

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 3 | fmaterialgroupid | 物料分类编码 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_im_warehousesetup_mater |  | fid |
| 2 | t_im_warehousesetup_mater_pkey |  | fentryid |

---

## 启用库存-主表 t_im_warehousesetup

- **表名称：** 启用库存-主表
- **表名：** t_im_warehousesetup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fisallowpartialneginv | 仅允许部分物料负库存 | bpchar | 1 |  | √ | '0' | 仅允许部分物料负库存 |
| 4 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 5 | forgid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 7 | finitstatus | 初始化状态 | varchar | 5 |  | √ | ' ' | 初始化状态,枚举: A :未初始化 B :已初始化 |
| 8 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 10 | ffinishinitdate | 结束初始化日期 | timestamp | 0 |  |  | null | 结束初始化日期 |
| 11 | fisallowallneginv | 允许全部物料负库存 | bpchar | 1 |  | √ | '0' | 允许全部物料负库存 |
| 12 | fstartstatus | 启用状态 | bpchar | 1 |  | √ | 'A' | 启用状态,枚举: A :未启用 B :已启用 |
| 13 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fsetuptime | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 17 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fisshow | 是否显示 | bpchar | 1 |  | √ | '0' | 是否显示 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_im_warehousesetup_pkey |  | fid |
| 2 | idx_im_warehousesetup_orgwh |  | forgid,fwarehouseid |

---

## 业务员-子表 t_im_warehousesetup_opera

- **表名称：** 业务员-子表
- **表名：** t_im_warehousesetup_opera

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foperatoruserid | 业务员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_im_warehousesetup_opera |  | fid |
| 2 | t_im_warehousesetup_opera_pkey |  | fentryid |
