# 项目物料共享变更单-mpm_xscroprojmatlsupply

## 共同供应单据体-子表 t_mpm_xssupplyentry

- **表名称：** 共同供应单据体-子表
- **表名：** t_mpm_xssupplyentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsupplyentrysrcid | 供应项目分录ID | int8 | 64 |  | √ | 0 | 供应项目分录ID |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fsupplyentrychangetype | 变更方式 | bpchar | 1 |  | √ | ' ' | 变更方式,枚举: A :新增 B :修改 C :删除 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fcomsupplyprojectid | 供应项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_xssupplyentry |  | fentryid |
| 2 | idx_mpm_xssupplyentry_fk |  | fid |

---

## 供应项目-多选基础资料表 t_mpm_xscroentrysuproj

- **表名称：** 供应项目-多选基础资料表
- **表名：** t_mpm_xscroentrysuproj

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_xscroentrysuproj |  | fpkid |
| 2 | idx_mpm_xsentrysuproj_fk |  | fentryid |

---

## 需求项目分类-多选基础资料表 t_mpm_xscrodemprojkind

- **表名称：** 需求项目分类-多选基础资料表
- **表名：** t_mpm_xscrodemprojkind

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [项目分类 bd_projectkind](../basedata_files/bd_projectkind.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_xscrodemprojkind |  | fpkid |
| 2 | idx_mpm_xscrodprojkd_fk |  | fid |

---

## 项目物料共享变更单-多语言表 t_mpm_xscroprojsupply_l

- **表名称：** 项目物料共享变更单-多语言表
- **表名：** t_mpm_xscroprojsupply_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fdescription | 描述 | varchar | 512 |  | √ | ' ' | 描述 |
| 4 | freason | 变更原因 | varchar | 512 |  | √ | ' ' | 变更原因 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 6 | fbillname | 方案名称 | varchar | 255 |  | √ | ' ' | 方案名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_xscroprojsupply_l |  | fpkid |
| 2 | idx_mpm_xscroprojsupply_l_fl |  | fid,flocaleid |

---

## 项目物料共享变更单-主表 t_mpm_xscroprojsupply

- **表名称：** 项目物料共享变更单-主表
- **表名：** t_mpm_xscroprojsupply

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsourcebillentity | 源单实体 | varchar | 80 |  | √ | ' ' | 源单实体 |
| 3 | forgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fchangestatus | 变更状态 | bpchar | 1 |  | √ | ' ' | 变更状态,枚举: A :正常 B :变更中 C :已变更 |
| 6 | factiverid | 生效人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fchangedate | 变更日期 | timestamp | 0 |  |  | null | 变更日期 |
| 9 | fbillno | 方案编码 | varchar | 80 |  | √ | ' ' | 方案编码 |
| 10 | fversion | 版本号 | varchar | 50 |  | √ | ' ' | 版本号 |
| 11 | factivedate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 12 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmatersharemethod | 物料共享方式 | bpchar | 1 |  | √ | 'A' | 物料共享方式,枚举: A :相互共享 B :使用共同的供应项目 C :自定义设置 |
| 14 | factivestatus | 生效状态 | bpchar | 1 |  | √ | ' ' | 生效状态,枚举: A :未生效 B :已生效 |
| 15 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | fprojectaddmethod | 项目添加方式 | bpchar | 1 |  | √ | ' ' | 项目添加方式,枚举: A :按单个项目 B :按项目分类 |
| 18 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 20 | fdescription | 描述 | varchar | 512 |  | √ | ' ' | 描述 |
| 21 | freason | 变更原因 | varchar | 512 |  | √ | ' ' | 变更原因 |
| 22 | fchangebizdate | 变更单日期 | timestamp | 0 |  |  | null | 变更单日期 |
| 23 | fbillname | 方案名称 | varchar | 255 |  | √ | ' ' | 方案名称 |
| 24 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 25 | fchangebillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 26 | fsubversion | 子版本号 | varchar | 50 |  | √ | ' ' | 子版本号 |
| 27 | fchangerid | 变更人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 28 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 29 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :启用 |
| 30 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 31 | fbilltype | fbilltype | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_xscroprojsupp_fbillno |  | fbillno |
| 2 | pk_mpm_xscroprojsupply |  | fid |

---

## 共同供应项目-多选基础资料表 t_mpm_xscrosupplyproject

- **表名称：** 共同供应项目-多选基础资料表
- **表名：** t_mpm_xscrosupplyproject

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_xscrosuproj_fk |  | fid |
| 2 | pk_mpm_xscrosupplyproject |  | fpkid |

---

## 需求项目-子表 t_mpm_xscroprojentry

- **表名称：** 需求项目-子表
- **表名：** t_mpm_xscroprojentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentrysrcid | 供需方案分录ID | int8 | 64 |  | √ | 0 | 供需方案分录ID |
| 3 | fprojectid | 需求项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fsupplyprojectid | fsupplyprojectid | int8 | 64 |  | √ | 0 |  |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fentrychangetype | 变更方式 | bpchar | 1 |  | √ | ' ' | 变更方式,枚举: A :新增 B :修改 C :删除 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_xscroprojentry_fk |  | fid |
| 2 | pk_mpm_xscroprojentry |  | fentryid |
