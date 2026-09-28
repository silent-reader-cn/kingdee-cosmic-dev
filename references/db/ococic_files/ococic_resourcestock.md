# 库存资源-ococic_resourcestock

## 库存资源-多语言表 t_ocdbd_res_stock_l

- **表名称：** 库存资源-多语言表
- **表名：** t_ocdbd_res_stock_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 资源名称 | varchar | 80 |  | √ | ' ' | 资源名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_res_stock_l |  | fpkid |
| 2 | t_ocdbd_resstockl_flid |  | fid,flocaleid |

---

## 库存资源-使用范围表 t_ocdbd_res_stock_u

- **表名称：** 库存资源-使用范围表
- **表名：** t_ocdbd_res_stock_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_ocdbd_res_stock_u_uo |  | fuseorgid |
| 2 | pk_t_ocdbd_res_stock_u |  | fdataid,fuseorgid |

---

## 库存资源-主表 t_ocdbd_res_stock

- **表名称：** 库存资源-主表
- **表名：** t_ocdbd_res_stock

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fresourceclassid | 库存资源类别 | int8 | 64 |  | √ | 0 | [库存资源类别 ococic_resourceclass](../ococic_files/ococic_resourceclass.md) |
| 3 | faddress | 详细地址 | varchar | 255 |  | √ | ' ' | 详细地址 |
| 4 | fprovincecityid | 仓库地址 | varchar | 36 |  | √ | ' ' | 仓库地址 |
| 5 | forgid | 使用组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 7 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstockstrategy | 库存策略 | bpchar | 1 |  | √ | '1' | 库存策略,枚举: 1 :共享 2 :分配+共享 3 :独享 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 14 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 15 | fchannelid | 渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 16 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | fname | fname | varchar | 80 |  | √ | ' ' |  |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fstockid | 企业仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 21 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fwarehouseid | 渠道仓库 | int8 | 64 |  | √ | 0 | [渠道仓库 ococic_warehouse](../ococic_files/ococic_warehouse.md) |
| 23 | fctrlstrategy | 共享策略 | varchar | 10 |  | √ | '5' | 共享策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 24 | fenable | 可用状态 | bpchar | 1 |  | √ | '1' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 25 | flongitude | 经度 | numeric | 23 | 10 | √ | 0 | 经度 |
| 26 | fnumber | 资源编码 | varchar | 80 |  | √ | ' ' | 资源编码 |
| 27 | fstockorgid | 企业库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 28 | flatitude | 纬度 | numeric | 23 | 10 | √ | 0 | 纬度 |
| 29 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 30 | fdelivertype | 支持配送方式 | varchar | 50 |  | √ | ' ' | 支持配送方式,枚举: 1 :配送 2 :自提 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_res_stock |  | fid |
| 2 | idx_t_ocdbd_res_stock_master |  | fmasterid |
| 3 | idx_ocdbd_resstock_num |  | fnumber |
| 4 | idx_t_ocdbd_res_stock_createorg |  | fcreateorgid |
