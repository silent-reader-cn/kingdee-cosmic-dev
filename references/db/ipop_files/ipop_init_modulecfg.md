# 初始化模块配置-ipop_init_modulecfg

## 初始化模块配置-主表 t_ipop_init_modulecfg

- **表名称：** 初始化模块配置-主表
- **表名：** t_ipop_init_modulecfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | findex | 排序 | int4 | 32 |  | √ | 0 | 排序 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | flicensegroup | 许可分组/模块 | int8 | 64 |  | √ | 0 | [模块许可分组配置 ipop_init_licgroupcfg](../ipop_files/ipop_init_licgroupcfg.md) |
| 7 | fneedassignment | 是否需要分配任务 | bpchar | 1 |  | √ | ' ' | 是否需要分配任务 |
| 8 | fbizfunctionkey | 检验的职能 | varchar | 50 |  | √ | ' ' | 检验的职能,枚举: all : fispurchase :采购职能 fissale :销售职能 fisproduce :生产职能 fisinventory :库存职能 fissettlement :结算职能 fisqc :质检职能 fisbankroll :收付职能 fisasset :资产职能 fistax :税务职能 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fdefault | 系统预置 | bpchar | 1 |  | √ | ' ' | 系统预置 |
| 11 | fchecklicense | 是否校验许可 | bpchar | 1 |  | √ | ' ' | 是否校验许可 |
| 12 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | ftype | 初始化类型 | bpchar | 1 |  | √ | ' ' | 初始化类型,枚举: 1 :系统初始化 2 :基础资料准备 3 :业务初始化 4 :对账 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | faccountingtype | 校验组织类型 | varchar | 10 |  | √ | ' ' | 校验组织类型,枚举: 0 : 1 :法人 2 :利润中心 |
| 17 | fcheckbizfunction | 是否校验职能 | bpchar | 1 |  | √ | ' ' | 是否校验职能 |
| 18 | fshowbyorg | 是否按组织显示 | bpchar | 1 |  | √ | ' ' | 是否按组织显示 |
| 19 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :启用 |
| 20 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 21 | fhasexceltpl | 支持下载模板 | bpchar | 1 |  | √ | ' ' | 支持下载模板 |
| 22 | fcheckaccounting | 是否校验核算组织 | bpchar | 1 |  | √ | ' ' | 是否校验核算组织 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ipop_init_modulecfg |  | fid |
| 2 | idx_ipop_init_modulecfg_num |  | fnumber |
| 3 | idx_ipop_init_modulecfg_type |  | ftype |

---

## 初始化模块配置-多语言表 t_ipop_init_modulecfg_l

- **表名称：** 初始化模块配置-多语言表
- **表名：** t_ipop_init_modulecfg_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ipop_init_modulecfg_l |  | fid,flocaleid |
| 2 | pk_t_ipop_init_modulecfg_l |  | fpkid |
