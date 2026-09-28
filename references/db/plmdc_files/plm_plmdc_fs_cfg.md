# 服务器配置-plm_plmdc_fs_cfg

## 单据体-子表 t_plmdc_fs_entity

- **表名称：** 单据体-子表
- **表名：** t_plmdc_fs_entity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fservername | 电子仓名称 | varchar | 50 |  | √ | ' ' | 电子仓名称 |
| 3 | fpublicaddress | 公网服务地址 | varchar | 50 |  | √ | ' ' | 公网服务地址 |
| 4 | fappsecret | App Secret | varchar | 128 |  | √ | ' ' | App Secret |
| 5 | fservernumber | 电子仓编码 | varchar | 50 |  | √ | ' ' | 电子仓编码 |
| 6 | ftestdetail | ftestdetail | varchar | 50 |  | √ | ' ' |  |
| 7 | fappkey | AppKey | varchar | 128 |  | √ | ' ' | AppKey |
| 8 | ftransfermode | 传输方式 | varchar | 50 |  | √ | ' ' | 传输方式,枚举: A :常规模式 B :快速模式 |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | frootpath | 主目录路径 | varchar | 50 |  | √ | ' ' | 主目录路径 |
| 11 | fintranetaddress | 服务地址 | varchar | 50 |  | √ | ' ' | 服务地址 |
| 12 | ftestresult | ftestresult | varchar | 50 |  | √ | ' ' |  |
| 13 | fmainserverflag | 是否主仓 | bpchar | 1 |  | √ | '0' | 是否主仓 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmdc_fs_entity_number |  | fservernumber |
| 2 | pk_plmdc_fs_entity |  | fentryid |

---

## 服务器配置-主表 t_plmdc_fs_cfg

- **表名称：** 服务器配置-主表
- **表名：** t_plmdc_fs_cfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fname | 服务器名称 | varchar | 50 |  | √ | ' ' | 服务器名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fappkey1 | AppKey | varchar | 50 |  | √ | ' ' | AppKey |
| 6 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 7 | fuseorg | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fcloudaddress | 云端服务器地址 | varchar | 50 |  | √ | ' ' | 云端服务器地址 |
| 10 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fstoragetype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: A :苍穹云存储 B :本地存储 |
| 12 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 13 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 14 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fappsecret1 | App Secret | varchar | 50 |  | √ | ' ' | App Secret |
| 18 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 19 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 20 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fcloudport | 端口号 | varchar | 50 |  | √ | ' ' | 端口号 |
| 22 | fnumber | 服务器编码 | varchar | 30 |  | √ | ' ' | 服务器编码 |
| 23 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmdc_fs_cfg_number |  | fnumber |
| 2 | pk_plmdc_fs_cfg |  | fid |
| 3 | idx_t_plmdc_fs_cfg_createorg |  | fcreateorgid |
| 4 | idx_t_plmdc_fs_cfg_master |  | fmasterid |

---

## 服务器配置-使用范围表 t_plmdc_fs_cfg_u

- **表名称：** 服务器配置-使用范围表
- **表名：** t_plmdc_fs_cfg_u

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
| 1 | idx_t_plmdc_fs_cfg_u_uo |  | fuseorgid |
| 2 | pk_t_plmdc_fs_cfg_u |  | fdataid,fuseorgid |

---

## 服务器配置-多语言表 t_plmdc_fs_cfg_l

- **表名称：** 服务器配置-多语言表
- **表名：** t_plmdc_fs_cfg_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 服务器名称 | varchar | 50 |  | √ | ' ' | 服务器名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmdc_fs_cfg_l_0 |  | fid,flocaleid |
| 2 | pk_plmdc_fs_cfg_l |  | fpkid |
