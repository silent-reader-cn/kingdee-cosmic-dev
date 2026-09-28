# 传输包管理-iptm_ct_datapacket

## 子包文件-附件表 t_iptm_ct_subpacket_fj

- **表名称：** 子包文件-附件表
- **表名：** t_iptm_ct_subpacket_fj

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 附件字段实体 bd_attachment |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_subpack_fj |  | fpkid |
| 2 | pk_t_iptm_ct_subpacket_fj |  | fentryid |

---

## 传输包管理-主表 t_iptm_ct_datapacket

- **表名称：** 传输包管理-主表
- **表名：** t_iptm_ct_datapacket

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 传输包名称 | varchar | 50 |  | √ | ' ' | 传输包名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fsrcdatacenter | 传输路径 | varchar | 500 |  | √ | ' ' | 传输路径 |
| 5 | fdestdatacenter | 目标数据中心 | varchar | 500 |  | √ | ' ' | 目标数据中心 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fsynmode | 通用配置项同步模式 | varchar | 50 |  | √ | ' ' | 通用配置项同步模式,枚举: RollbackOnError :错误时全部回滚 ResumeOnError :错误时忽略 |
| 8 | flockedstatus | 锁定状态 | varchar | 50 |  | √ | ' ' | 锁定状态,枚举: 0 :未锁定 1 :已锁定 |
| 9 | fsyncstate | 同步状态 | varchar | 50 |  | √ | ' ' | 同步状态,枚举: 0 :未同步 1 :已同步 2 :同步失败 3 :同步未完成 |
| 10 | fremarks | 备注 | varchar | 2000 |  | √ | ' ' | 备注 |
| 11 | fpacketversion | 上线版本 | int8 | 64 |  | √ | 0 | 上线版本 iptm_ct_version |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fstatus | 传输包状态 | varchar | 50 |  | √ | ' ' | 传输包状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fpackettype | 传输包类型 | varchar | 50 |  | √ | ' ' | 传输包类型,枚举: 1 :基础配置 2 :元数据 |
| 17 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 0 :手工新增 1 :手工上传 2 :在线传输 |
| 19 | fallowchange | 不允许修改 | bpchar | 1 |  | √ | ' ' | 不允许修改 |
| 20 | fnumber | 传输包编码 | varchar | 80 |  | √ | ' ' | 传输包编码 |
| 21 | fsubpacketcount | 子传输包个数 | int8 | 64 |  | √ | 0 | 子传输包个数 |
| 22 | fdltrcount | 下载传输次数 | int8 | 64 |  | √ | 0 | 下载传输次数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_iptm_ct_datapacket |  | fid |
| 2 | idx_datapacket |  | fnumber |

---

## 子传输包-子表 t_iptm_ct_subdatapacket

- **表名称：** 子传输包-子表
- **表名：** t_iptm_ct_subdatapacket

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 3 | fbizobject | 业务对象 | int8 | 64 |  | √ | 0 | 传输对象 iptm_ct_configitems |
| 4 | fsyncstate | 同步状态 | varchar | 50 |  | √ | ' ' | 同步状态,枚举: 0 :未同步 1 :同步完成 2 :同步失败 |
| 5 | fentrystatus | 子包状态 | varchar | 50 |  | √ | ' ' | 子包状态,枚举: 0 :正常 1 :作废 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | frelylevel | 依赖层级 | int8 | 64 |  | √ | 0 | 依赖层级 |
| 8 | fcustparam | 自定义参数 | varchar | 255 |  | √ | ' ' | 自定义参数 |
| 9 | fpacketdata | 子包数据 | varchar | 255 |  | √ | ' ' | 子包数据 |
| 10 | fpacketdata_tag | 子包数据_详情 | text | 0 |  |  | null | 子包数据_详情 |
| 11 | fsubpackettype | fsubpackettype | varchar | 50 |  | √ | ' ' |  |
| 12 | ffilename | 文件名 | varchar | 50 |  | √ | ' ' | 文件名 |
| 13 | fupdatetime | 更新日期 | timestamp | 0 |  |  | null | 更新日期 |
| 14 | fcustparam_tag | 自定义参数_详情 | text | 0 |  |  | null | 自定义参数_详情 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_subpacket |  | fid |
| 2 | pk_t_iptm_ct_subdatapacket |  | fentryid |

---

## 传输包管理-多语言表 t_iptm_ct_datapacket_l

- **表名称：** 传输包管理-多语言表
- **表名：** t_iptm_ct_datapacket_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 传输包名称 | varchar | 50 |  | √ | ' ' | 传输包名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_iptm_ct_datapacket_l |  | fpkid |
| 2 | idx_iptm_ct_datapacket_l |  | fid,flocaleid |
