# 定标份额分配方式变更-src_ratiotypechg

## 定标份额分配方式变更-主表 t_src_ratiotypechg

- **表名称：** 定标份额分配方式变更-主表
- **表名：** t_src_ratiotypechg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbidchangeid | 寻源项目变更F7 | int8 | 64 |  | √ | 0 | [寻源项目变更F7 src_bidchangef7](../pds_files/src_bidchangef7.md) |
| 3 | fprojectid | 寻源项目F7 | int8 | 64 |  | √ | 0 | [招标项目F7 src_projectf7](../src_files/src_projectf7.md) |
| 4 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fchgsrcbillid | 变更源单ID | int8 | 64 |  | √ | 0 | 变更源单ID |
| 7 | forgid | 主业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fentitykey | 组件标识 | varchar | 50 |  | √ | ' ' | 组件标识 |
| 9 | fcompbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 10 | fpentitykey | 父单据标识 | varchar | 50 |  | √ | ' ' | 父单据标识 |
| 11 | fnewratiotype | 定标份额分配方式(变更后) | varchar | 50 |  | √ | ' ' | 定标份额分配方式(变更后),枚举: 1 :手工分配份额 2 :自动分配份额(按项目) 3 :自动分配份额(按标段) 4 :自动分配份额(按标的) 9 :不需要份额分配与控制 |
| 12 | fratiotype | 定标份额分配方式(变更前) | varchar | 50 |  | √ | ' ' | 定标份额分配方式(变更前),枚举: 1 :手工分配份额 2 :自动分配份额(按项目) 3 :自动分配份额(按标段) 4 :自动分配份额(按标的) 9 :不需要份额分配与控制 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_ratiotypechg_pid |  | fparentid |
| 2 | pk_src_ratiotypechg |  | fid |

---

## 份额分配比率-子表 t_src_ratiotypechgentry

- **表名称：** 份额分配比率-子表
- **表名：** t_src_ratiotypechgentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forderratio06 | 第六名份额(%) | numeric | 23 | 10 | √ | 0 | 第六名份额(%) |
| 3 | ftrainqty | 培养供应商数 | int4 | 32 |  | √ | 0 | 培养供应商数 |
| 4 | forderratio05 | 第五名份额(%) | numeric | 23 | 10 | √ | 0 | 第五名份额(%) |
| 5 | forderratio08 | 第八名份额(%) | numeric | 23 | 10 | √ | 0 | 第八名份额(%) |
| 6 | fprojectid | 寻源项目 | int8 | 64 |  | √ | 0 | [招标项目F7 src_projectf7](../src_files/src_projectf7.md) |
| 7 | forderratio07 | 第七名份额(%) | numeric | 23 | 10 | √ | 0 | 第七名份额(%) |
| 8 | forderratio09 | 第九名份额(%) | numeric | 23 | 10 | √ | 0 | 第九名份额(%) |
| 9 | falterqty | 备选供应商数 | int4 | 32 |  | √ | 0 | 备选供应商数 |
| 10 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 11 | fwinerqty | 中标供应商数 | int4 | 32 |  | √ | 0 | 中标供应商数 |
| 12 | forderratio10 | 第十名份额(%) | numeric | 23 | 10 | √ | 0 | 第十名份额(%) |
| 13 | fpurlistid | 标的名称 | int8 | 64 |  | √ | 0 | 采购清单F7 src_purlistf7 |
| 14 | forderratio02 | 第二名份额(%) | numeric | 23 | 10 | √ | 0 | 第二名份额(%) |
| 15 | forderratio01 | 第一名份额(%) | numeric | 23 | 10 | √ | 0 | 第一名份额(%) |
| 16 | forderratio04 | 第四名份额(%) | numeric | 23 | 10 | √ | 0 | 第四名份额(%) |
| 17 | forderratio03 | 第三名份额(%) | numeric | 23 | 10 | √ | 0 | 第三名份额(%) |
| 18 | fsurplusratio | 剩余份额分配方式 | bpchar | 1 |  | √ | '1' | 剩余份额分配方式,枚举: 1 :分配给第一名供应商 2 :按中标供应商份额权重分摊 3 :在中标供应商间平均分摊 9 :不需要处理 |
| 19 | fpackageid | 标段名称 | int8 | 64 |  | √ | 0 | [标段名称 src_packagef7](../src_files/src_packagef7.md) |
| 20 | forderratio | 份额合计(%) | numeric | 23 | 10 | √ | 0 | 份额合计(%) |
| 21 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_ratiotypechgentry_pid |  | fprojectid |
| 2 | idx_src_ratiotypechgentry_fid |  | fid |
| 3 | pk_src_ratiotypechgentry |  | fentryid |
