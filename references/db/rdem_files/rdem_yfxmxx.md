# 研发项目信息-rdem_yfxmxx

## 申报项目信息-多选基础资料表 t_rdem_yfxmxx_sbxmxx

- **表名称：** 申报项目信息-多选基础资料表
- **表名：** t_rdem_yfxmxx_sbxmxx

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [申报项目信息 rdem_sbxmxx](../rdem_files/rdem_sbxmxx.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rdem_yfxmxx_sbxmxx |  | fpkid |
| 2 | idx_rdem_yfxmxx_sbxmxx_fk |  | fid |

---

## 研发项目信息-主表 t_rdem_yfxmxx

- **表名称：** 研发项目信息-主表
- **表名：** t_rdem_yfxmxx

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fxmle | 项目类型 | varchar | 50 |  | √ | ' ' | 项目类型,枚举: zzyf :自主研发 wtyf :委托研发 jzyf :集中研发 hzyf :合作研发 |
| 3 | fhzf | 合作方 | varchar | 200 |  | √ | ' ' | 合作方 |
| 4 | fgatherendtime | 费用归集结束时间 | timestamp | 0 |  |  | null | 费用归集结束时间 |
| 5 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fysxmdx | 映射项目对象 | varchar | 50 |  | √ | ' ' | 映射项目对象,枚举: bos_costcenter :成本中心 bd_project :项目 |
| 7 | fsbxmxxid | 申报项目信息(废弃) | int8 | 64 |  | √ | 0 | [申报项目信息 rdem_sbxmxx](../rdem_files/rdem_sbxmxx.md) |
| 8 | fstfsfglqy | 受托方是否关联企业 | bpchar | 1 |  | √ | '0' | 受托方是否关联企业 |
| 9 | fbaseproject | 研发项目编号 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fxmms | 项目描述 | varchar | 1000 |  | √ | ' ' | 项目描述 |
| 15 | fend | 项目结束时间 | timestamp | 0 |  |  | null | 项目结束时间 |
| 16 | fgjysz | 归集要素值（废弃） | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 17 | fsfjwstf | 是否境外受托方 | bpchar | 1 |  | √ | '0' | 是否境外受托方 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 20 | fgjyslx | 归集要素类型（废弃） | varchar | 50 |  | √ | ' ' | 归集要素类型（废弃）,枚举: bos_costcenter :成本中心 bd_project :项目 |
| 21 | fsfkjjkc | 是否可加计扣除 | varchar | 50 |  | √ | ' ' | 是否可加计扣除,枚举: 1 :是 2 :否 0 :待识别 |
| 22 | fstart | 项目起始时间 | timestamp | 0 |  |  | null | 项目起始时间 |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | fpaytype | 支出类型 | varchar | 50 |  | √ | ' ' | 支出类型,枚举: capital :资本化 cost :费用化 |
| 25 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 1 :模板导入 2 :手工新增 3 :系统同步 |
| 26 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 27 | fnumber | 研发项目编号 | varchar | 30 |  | √ | ' ' | 研发项目编号 |
| 28 | fxmfzr | 项目负责人 | varchar | 200 |  | √ | ' ' | 项目负责人 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rdem_yfxmxx_m0 |  | fmasterid |
| 2 | pk_rdem_yfxmxx |  | fid |

---

## 映射项目值-多选基础资料表 t_rdem_yfxm_costcenter

- **表名称：** 映射项目值-多选基础资料表
- **表名：** t_rdem_yfxm_costcenter

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rdem_yfxm_costcenter |  | fpkid |
| 2 | idx_rdem_yfxm_costcenter_fk |  | fid |

---

## 研发项目信息-多语言表 t_rdem_yfxmxx_l

- **表名称：** 研发项目信息-多语言表
- **表名：** t_rdem_yfxmxx_l

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
| 1 | idx_rdem_yfxmxx_l_0 |  | fid,flocaleid |
| 2 | pk_rdem_yfxmxx_l |  | fpkid |
