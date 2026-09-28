# 项目物料共享-mpm_croprojmatlsupply

## 供应项目-多选基础资料表 t_mpm_croentrysuproj

- **表名称：** 供应项目-多选基础资料表
- **表名：** t_mpm_croentrysuproj

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
| 1 | pk_mpm_croentrysuproj |  | fpkid |
| 2 | idx_mpm_croentrysuproj_fk |  | fentryid |

---

## 项目物料共享-主表 t_mpm_croprojsupply

- **表名称：** 项目物料共享-主表
- **表名：** t_mpm_croprojsupply

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fmatersharemethod | 物料共享方式 | bpchar | 1 |  | √ | 'A' | 物料共享方式,枚举: A :相互共享 B :使用共同的供应项目 C :自定义设置 |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fprojectaddmethod | 项目添加方式 | bpchar | 1 |  | √ | ' ' | 项目添加方式,枚举: A :按单个项目 B :按项目分类 |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fdescription | 描述 | varchar | 512 |  | √ | ' ' | 描述 |
| 10 | fbillname | 方案名称 | varchar | 255 |  | √ | ' ' | 方案名称 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fchangestatus | 变更状态 | bpchar | 1 |  | √ | ' ' | 变更状态,枚举: A :正常 B :变更中 C :已变更 |
| 13 | fsubversion | 子版本号 | varchar | 50 |  | √ | ' ' | 子版本号 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fchangerid | 变更人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fchangedate | 变更日期 | timestamp | 0 |  |  | null | 变更日期 |
| 17 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :启用 |
| 18 | fbillno | 方案编码 | varchar | 80 |  | √ | ' ' | 方案编码 |
| 19 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fversion | 版本号 | varchar | 50 |  | √ | ' ' | 版本号 |
| 21 | fbilltype | fbilltype | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_croprojsupply |  | fid |
| 2 | idx_mpm_croprojsupply_fb |  | fbillno |

---

## 共同供应项目-多选基础资料表 t_mpm_crosupplyproject

- **表名称：** 共同供应项目-多选基础资料表
- **表名：** t_mpm_crosupplyproject

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
| 1 | pk_mpm_crosupplyproject |  | fpkid |
| 2 | idx_mpm_crosupproj_fk |  | fid |

---

## 项目物料共享-多语言表 t_mpm_croprojsupply_l

- **表名称：** 项目物料共享-多语言表
- **表名：** t_mpm_croprojsupply_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fdescription | 描述 | varchar | 512 |  | √ | ' ' | 描述 |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fbillname | 方案名称 | varchar | 255 |  | √ | ' ' | 方案名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_croprojsupply_l_fl |  | fid,flocaleid |
| 2 | pk_mpm_croprojsupply_l |  | fpkid |

---

## 需求项目-子表 t_mpm_croprojentry

- **表名称：** 需求项目-子表
- **表名：** t_mpm_croprojentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprojectid | 需求项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fsupplyprojectid | fsupplyprojectid | int8 | 64 |  | √ | 0 |  |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_croprojentry |  | fentryid |
| 2 | idx_mpm_croprojentry_fk |  | fid |

---

## 需求项目分类-多选基础资料表 t_mpm_crodemprojkind

- **表名称：** 需求项目分类-多选基础资料表
- **表名：** t_mpm_crodemprojkind

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
| 1 | idx_mpm_crodprojkind_fk |  | fid |
| 2 | pk_mpm_crodemprojkind |  | fpkid |

---

## 共同供应单据体-子表 t_mpm_supplyentry

- **表名称：** 共同供应单据体-子表
- **表名：** t_mpm_supplyentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | fcomsupplyprojectid | 供应项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_supplyentry_fk |  | fid |
| 2 | pk_mpm_supplyentry |  | fentryid |
