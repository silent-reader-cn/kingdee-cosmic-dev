# 首页界面显示方案-osr_pad_displayscheme

## 首页界面显示方案-多语言表 t_osr_homeconfig_l

- **表名称：** 首页界面显示方案-多语言表
- **表名：** t_osr_homeconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 方案名称 | varchar | 240 |  | √ | ' ' | 方案名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_osr_homeconfig_l |  | fid,flocaleid |
| 2 | pk_t_osr_homeconfig_l |  | fpkid |

---

## 适用车间-多选基础资料表 t_osr_homeconfig_org

- **表名称：** 适用车间-多选基础资料表
- **表名：** t_osr_homeconfig_org

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_osr_homeconfig_org |  | fpkid |
| 2 | osr_homeconfig_org_idx |  | fid,fbasedataid |

---

## 首页界面显示方案-主表 t_osr_homeconfig

- **表名称：** 首页界面显示方案-主表
- **表名：** t_osr_homeconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 方案名称 | varchar | 100 |  | √ | ' ' | 方案名称 |
| 3 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 9 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 10 | fworkshoporg | fworkshoporg | int8 | 64 |  | √ | 0 |  |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fdefaultscheme | 发布 | bpchar | 1 |  | √ | '0' | 发布 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_osr_homeconfig |  | fworkshoporg |
| 2 | pk_t_osr_homeconfig |  | fid |

---

## 主页配置-多语言表 t_osr_homeconfig_entry_l

- **表名称：** 主页配置-多语言表
- **表名：** t_osr_homeconfig_entry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | ffieldremark | 功能备注 | varchar | 1500 |  | √ | ' ' | 功能备注 |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_osr_homeconfig_entry_l |  | fentryid,flocaleid |
| 2 | pk_t_osr_homeconfig_entry_l |  | fpkid |

---

## 主页配置-子表 t_osr_homeconfig_entry

- **表名称：** 主页配置-子表
- **表名：** t_osr_homeconfig_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseqnumber | 顺序号 | int4 | 32 |  | √ | 0 | 顺序号 |
| 3 | fcardname | 平板显示名称 | varchar | 100 |  | √ | ' ' | 平板显示名称 |
| 4 | fhomecard | 功能 | int8 | 64 |  | √ | 0 | [平板首页功能 osr_pad_functionconfig](../osr_files/osr_pad_functionconfig.md) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | ffieldremark | 功能备注 | varchar | 1000 |  | √ | ' ' | 功能备注 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fvisibility | 可见性 | bpchar | 1 |  | √ | '1' | 可见性 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_osr_homeconfig_entry |  | fhomecard |
| 2 | pk_t_osr_homeconfig_entry |  | fentryid |
