# 制造云服务配置-mpdm_atmocfg

## 制造云服务单据体-子表 t_mpdm_atmocfgentry

- **表名称：** 制造云服务单据体-子表
- **表名：** t_mpdm_atmocfgentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finparam | 参数 | varchar | 2000 |  | √ | ' ' | 参数 |
| 3 | fdataentityid | 数据对象主键 | varchar | 50 |  | √ | ' ' | 数据对象主键 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fissetinparam | 已设置参数 | bpchar | 1 |  | √ | ' ' | 已设置参数 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fatmop | 制造云服务 | int8 | 64 |  | √ | 0 | [制造云服务 mpdm_atmoservice](../mpdm_files/mpdm_atmoservice.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_atmocfgentry |  | fid,fseq |
| 2 | t_mpdm_atmocfgentry_pkey |  | fentryid |

---

## 制造云服务配置-多语言表 t_mpdm_atmocfg_l

- **表名称：** 制造云服务配置-多语言表
- **表名：** t_mpdm_atmocfg_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 操作名 | varchar | 100 |  | √ | ' ' | 操作名 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_mpdm_atmocfg_l_pkey |  | fpkid |
| 2 | idx_mpdm_atmocfg_l |  | fid,flocaleid |

---

## 制造云服务配置-主表 t_mpdm_atmocfg

- **表名称：** 制造云服务配置-主表
- **表名：** t_mpdm_atmocfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fgroupid | 所属单据 | int8 | 64 |  | √ | 0 | [制造云服务配置分组 mpdm_atmocfggp](../mpdm_files/mpdm_atmocfggp.md) |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 9 | fnumber | 操作标识 | varchar | 30 |  | √ | ' ' | 操作标识 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_atmocfg |  | fnumber,fgroupid |
| 2 | t_mpdm_atmocfg_pkey |  | fid |
