# 按需采购条件设置-pm_odpurcondition

## 物料分类-多选基础资料表 t_pm_odpurmaterialgroup

- **表名称：** 物料分类-多选基础资料表
- **表名：** t_pm_odpurmaterialgroup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pm_odpurmaterialgroup |  | fpkid |
| 2 | idx_pm_odpur_mg_fid |  | fid |
| 3 | idx_pm_odpur_mg_fbdid |  | fbasedataid |

---

## 物料编码-多选基础资料表 t_pm_odpurmaterial

- **表名称：** 物料编码-多选基础资料表
- **表名：** t_pm_odpurmaterial

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_odpur_material_fbdid |  | fbasedataid |
| 2 | idx_pm_odpur_material_fid |  | fid |
| 3 | pk_t_pm_odpurmaterial |  | fpkid |

---

## 仓库-多选基础资料表 t_pm_odpurwarehouse

- **表名称：** 仓库-多选基础资料表
- **表名：** t_pm_odpurwarehouse

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_odpur_warehouse_fbdid |  | fbasedataid |
| 2 | idx_pm_odpur_warehouse_fid |  | fid |
| 3 | pk_t_pm_odpurwarehouse |  | fpkid |

---

## 按需采购条件设置-主表 t_pm_odpurcondition

- **表名称：** 按需采购条件设置-主表
- **表名：** t_pm_odpurcondition

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | ffromsupplydate | 供应日期.开始 | timestamp | 0 |  |  | null | 供应日期.开始 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | LOCALTIMESTAMP | 创建时间 |
| 5 | fdemandorg | 需求组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fpurplanscheme | 计划方案 | int8 | 64 |  | √ | 0 | [计划方案 pm_planschemeconfig](../pm_files/pm_planschemeconfig.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fschemename | 方案名称 | varchar | 50 |  | √ | ' ' | 方案名称 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | ftodemanddate | 需求日期.结束 | timestamp | 0 |  |  | null | 需求日期.结束 |
| 11 | ffromdemanddate | 需求日期.开始 | timestamp | 0 |  |  | null | 需求日期.开始 |
| 12 | fdemandbilltype | 需求单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 13 | ftosupplydate | 供应日期.结束 | timestamp | 0 |  |  | null | 供应日期.结束 |
| 14 | fpurorg | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fmaterialattr | 物料属性 | varchar | 25 |  | √ | '10040' | 物料属性,枚举: 10030 :自制 10040 :外购 10050 :委外 10020 :虚拟 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_odpur_purplanscheme |  | fpurplanscheme |
| 2 | pk_t_pm_odpurcondition |  | fid |

---

## 库存组织-多选基础资料表 t_pm_odpurinvorg

- **表名称：** 库存组织-多选基础资料表
- **表名：** t_pm_odpurinvorg

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
| 1 | idx_pm_odpur_invorg_fid |  | fid |
| 2 | pk_t_pm_odpurinvorg |  | fpkid |
| 3 | idx_pm_odpur_invorg_fbdid |  | fbasedataid |

---

## 存货类别-多选基础资料表 t_pm_odpurmatcategory

- **表名称：** 存货类别-多选基础资料表
- **表名：** t_pm_odpurmatcategory

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [存货类别 bd_materialcategory](../basedata_files/bd_materialcategory.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_odpur_ppmc_fbdid |  | fbasedataid |
| 2 | idx_pm_odpur_pmc_fid |  | fid |
| 3 | pk_t_pm_odpurmatcategory |  | fpkid |

---

## 供应组织-多选基础资料表 t_pm_odpursupplyorg

- **表名称：** 供应组织-多选基础资料表
- **表名：** t_pm_odpursupplyorg

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
| 1 | pk_t_pm_odpursupplyorg |  | fpkid |
| 2 | idx_pm_odpur_supplyorg_fid |  | fid |
| 3 | idx_pm_odpur_supplyorg_fbdid |  | fbasedataid |
