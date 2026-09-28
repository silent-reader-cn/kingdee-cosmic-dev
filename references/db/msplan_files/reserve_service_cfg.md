# 预留服务配置-reserve_service_cfg

## 预留服务配置-多语言表 t_reserve_service_l

- **表名称：** 预留服务配置-多语言表
- **表名：** t_reserve_service_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 512 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_reserve_service_ln |  | fid,flocaleid |
| 2 | pk_t_reserve_service_l |  | fpkid |

---

## 单据体-子表 t_reserve_serviceentry

- **表名称：** 单据体-子表
- **表名：** t_reserve_serviceentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fforcerelease | 强制释放 | bpchar | 1 |  | √ | '0' | 强制释放 |
| 4 | foperation | 操作 | varchar | 36 |  | √ | ' ' | 操作 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_reserve_serviceentry |  | fentryid |
| 2 | idx_reserve_service_e |  | fid |

---

## 预留服务配置-主表 t_reserve_service

- **表名称：** 预留服务配置-主表
- **表名：** t_reserve_service

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fgroupid | 预留服务 | int8 | 64 |  | √ | 0 | [预留服务分组 reserve_servicegroup](../msplan_files/reserve_servicegroup.md) |
| 5 | fbillobject | 单据对象 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | freservetype | 预留类型 | varchar | 10 |  | √ | ' ' | 预留类型,枚举: 1 :强预留 0 :弱预留 |
| 8 | fissysinit | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 9 | fisinv | 库存单据 | bpchar | 1 |  | √ | '0' | 库存单据 |
| 10 | fdescription | 描述 | varchar | 512 |  | √ | ' ' | 描述 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fbilloperation | 单据操作 | varchar | 200 |  | √ | ' ' | 单据操作,枚举: |
| 13 | fstatus | 数据状态 | varchar | 10 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | f_filter_value | 过滤器值 | varchar | 512 |  | √ | ' ' | 过滤器值 |
| 17 | freleasetype | 释放类型 | varchar | 20 |  | √ | ' ' | 释放类型,枚举: 1 :关闭 2 :释放 |
| 18 | f_filter_value_tag | 过滤器值_详情 | varchar | 512 |  | √ | ' ' | 过滤器值_详情 |
| 19 | fenable | 使用状态 | varchar | 10 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fnumber | 编码 | varchar | 120 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_reserve_service |  | fgroupid,fbilloperation,fbillobject |
| 2 | pk_t_reserve_service |  | fid |
