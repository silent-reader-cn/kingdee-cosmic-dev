# 地址管理设置-cts_advance_address

## 地图接口字段映射单据体-子表 t_cts_mapfieldmapping

- **表名称：** 地图接口字段映射单据体-子表
- **表名：** t_cts_mapfieldmapping

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fadmindivisionnumber | 行政区划编码字段 | varchar | 50 |  | √ | ' ' | 行政区划编码字段,枚举: |
| 3 | fmapinterfacefield | 地图接口字段 | varchar | 255 |  | √ | ' ' | 地图接口字段 |
| 4 | fmaptipsfield | 地点提示字段 | varchar | 255 |  | √ | ' ' | 地点提示字段 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | faddressconfigfield | 地址格式字段 | varchar | 50 |  | √ | ' ' | 地址格式字段,枚举: |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cts_mapfieldmapping |  | fentryid |
| 2 | idx_cts_mapfiemapping |  | fid |

---

## 地址管理设置-多语言表 t_cts_advanceaddress_l

- **表名称：** 地址管理设置-多语言表
- **表名：** t_cts_advanceaddress_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cts_advanceaddress_l |  | fpkid |
| 2 | idx_cts_aal_fid |  | fid |

---

## 地址管理设置-主表 t_cts_advanceaddress

- **表名称：** 地址管理设置-主表
- **表名：** t_cts_advanceaddress

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fstatus | 数据状态 | varchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 9 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 10 | fenablefeature | 启用特性 | bpchar | 1 |  | √ | '0' | 启用特性 |
| 11 | fenablemap | 启用地图组件 | bpchar | 1 |  | √ | '0' | 启用地图组件 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cts_advanceaddress |  | fid |
| 2 | idx_cts_aa_fnumber |  | fnumber |

---

## 单据体-子表 t_cts_addressmoveconfig

- **表名称：** 单据体-子表
- **表名：** t_cts_addressmoveconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdetailaddresskey | 详细地址字段 | varchar | 50 |  | √ | ' ' | 详细地址字段 |
| 3 | fadmindivisionkey | 行政区划字段 | varchar | 50 |  | √ | ' ' | 行政区划字段 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fbillkey | 单据 | varchar | 50 |  | √ | ' ' | 实体元数据 bos_entitymeta |
| 7 | fsyncstatus | 同步状态 | varchar | 50 |  | √ | ' ' | 同步状态,枚举: 0 :未同步 1 :同步中 2 :同步成功 3 :同步异常 |
| 8 | faddresskey | 高级地址字段 | varchar | 50 |  | √ | ' ' | 高级地址字段 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cts_amc_fid |  | fid |
| 2 | pk_t_cts_addressmoveconfig |  | fentryid |

---

## 地图配置单据体-子表 t_cts_mapconfigentry

- **表名称：** 地图配置单据体-子表
- **表名：** t_cts_mapconfigentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmapkey_enp | fmapkey_enp | text | 0 |  |  | null |  |
| 3 | fmapconfigtype | 接口 | varchar | 50 |  | √ | ' ' | 接口,枚举: 0 :地理编码 1 :逆地理编码 2 :地点输入提示 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fconnstatus | 连接状态 | varchar | 50 |  | √ | ' ' | 连接状态,枚举: 0 :连接成功 1 :连接失败 |
| 6 | fdescription | 描述 | varchar | 50 |  | √ | ' ' | 描述 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fmapkey | 秘钥 | varchar | 50 |  | √ | ' ' | 秘钥 |
| 9 | fmapurl | 请求url | varchar | 255 |  | √ | ' ' | 请求url |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cts_mapconfigentry |  | fentryid |
| 2 | idx_cts_mapconfentry |  | fid |
