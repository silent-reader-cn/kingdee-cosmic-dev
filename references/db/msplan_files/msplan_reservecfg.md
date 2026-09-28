# 净改变服务配置-msplan_reservecfg

## 单据体-子表 t_msplan_reservecfgentry

- **表名称：** 单据体-子表
- **表名：** t_msplan_reservecfgentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | foperation | 操作 | varchar | 60 |  | √ | ' ' | 操作 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msplan_reservecfgentry |  | fentryid |
| 2 | idx_msplan_reservecfgentry |  | fid,fseq |

---

## 净改变服务配置-主表 t_msplan_reservecfg

- **表名称：** 净改变服务配置-主表
- **表名：** t_msplan_reservecfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fgroupid | 净改变服务 | int8 | 64 |  | √ | 0 | 净改变服务配置分组 msplan_reservecfg_group |
| 4 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 5 | fbillobject | 单据对象 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fresourceid | 来源服务ID | int8 | 64 |  | √ | 0 | 来源服务ID |
| 8 | ffiltervalue | 过滤器值 | varchar | 255 |  | √ | ' ' | 过滤器值 |
| 9 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fbilloperation | 单据操作 | varchar | 512 |  | √ | ' ' | 单据操作,枚举: |
| 12 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fresourcetype | 来源类型 | varchar | 30 |  | √ | ' ' | 来源类型,枚举: 0 :手工新增 1 :供应链 2 :系统预设 |
| 16 | ffiltervalue_tag | 过滤器值_详情 | text | 0 |  |  | null | 过滤器值_详情 |
| 17 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msplan_reservecfg |  | fnumber |
| 2 | idx_msplan_reservecfg_b |  | fbillobject |
| 3 | pk_msplan_reservecfg |  | fid |

---

## 净改变服务配置-多语言表 t_msplan_reservecfg_l

- **表名称：** 净改变服务配置-多语言表
- **表名：** t_msplan_reservecfg_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msplan_reservecfg_l |  | fid,flocaleid |
| 2 | pk_msplan_reservecfg_l |  | fpkid |
